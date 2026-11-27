import re
import pandas as pd

# 1. Load the dataset (e.g., from 04_VALIDATION or 01_RAW/filmwebplus)
df = pd.read_csv("./data/04_VALIDATION/data.csv", encoding="utf-8-sig")

# Remove unnecessary index columns (e.g., ,Unnamed: 0)
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

# 2. Keyword dictionaries (word stems for Polish movie reviews)
positive_words = [
    r"świetn\w*", r"dobr\w*", r"rewelacyjn\w*", r"genialn\w*", r"arcydzieł\w*",
    r"polecam", r"wciągając\w*", r"klimatyczn\w*", r"wzruszając\w*", r"zabawn\w*",
    r"super", r"doskonał\w*", r"wybitn\w*", r"majstersztyk\w*", r"warto",
    r"piękn\w*", r"mistrzowsk\w*", r"zachwycając\w*", r"poruszając\w*", r"ciekaw\w*"
]

negative_words = [
    r"słab\w*", r"nudn\w*", r"beznadziejn\w*", r"tragiczn\w*", r"gniot\w*",
    r"dno", r"rozczarowani\w*", r"strata czasu", r"kiepsk\w*", r"okropn\w*",
    r"koszmar\w*", r"żenując\w*", r"przewidywaln\w*", r"sztuczn\w*", r"fataln\w*",
    r"nie polecam", r"szmir\w*", r"badziew\w*", r"nużąc\w*", r"płytk\w*"
]

# Compile regular expressions (case-insensitive, \b denotes word boundaries)
pos_pattern = re.compile(r"\b(?:" + "|".join(positive_words) + r")\b", re.IGNORECASE)
neg_pattern = re.compile(r"\b(?:" + "|".join(negative_words) + r")\b", re.IGNORECASE)

# 3. Function to analyze a single row/review (returns score and label: 0, 1, or 2)
def analyze_sentiment(text):
    if not isinstance(text, str):
        return 0, 1  # Missing or non-string text -> neutral (1)
    
    pos_count = len(pos_pattern.findall(text))
    neg_count = len(neg_pattern.findall(text))
    score = pos_count - neg_count
    
    if score > 0:
        label = 2  # positive
    elif score < 0:
        label = 0  # negative
    else:
        label = 1  # neutral
        
    return score, label

# 4. Apply the function row by row
results = df["review"].apply(analyze_sentiment)
df["score"] = [res[0] for res in results]
df["predicted_sentiment"] = [res[1] for res in results]

# Reorder columns: review -> score -> prediction -> ground truth sentiment at the end
df = df[["review", "score", "predicted_sentiment", "sentiment"]]

# Preview the first 10 rows
print(df.head(10))

# Calculate accuracy on labelled reviews (excluding -1)
labelled = df[df["sentiment"] != -1]
if not labelled.empty:
    accuracy = (labelled["predicted_sentiment"] == labelled["sentiment"]).mean() * 100
    print(f"\nBaseline Accuracy on labelled set: {accuracy:.2f}%")

# Save the results to a new CSV file
# df.to_csv("./data/04_VALIDATION/data_scored.csv", index=False, encoding="utf-8-sig")