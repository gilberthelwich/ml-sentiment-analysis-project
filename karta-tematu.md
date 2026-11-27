# Karta zgłoszenia tematu projektu

**Grupa:** L3 (niestacjonarna) · **Zespół:** Z1 · **Data ostatniej zmiany:** 18.11.2026
Sztuczna inteligencja — laboratorium · Collegium Da Vinci · rok akad. 2026/2027

## 1. Skład zespołu (obowiązkowe)

|Imię i nazwisko|Nr albumu|Rola w zespole|
|---|---|---|
|Gilbert Helwich|24546|współodpowiedzialny za całość: dane, implementacja, ewaluacja, dokumentacja|
|Dawid Ślusarczyk|31077|współodpowiedzialny za całość: dane, implementacja, ewaluacja, dokumentacja|


## 2. Tytuł

- **Po polsku:** Klasyfikator wydźwięku recenzji filmowych
- **Po angielsku:** Movie Review Sentiment Classifier

## 3. Problem (obowiązkowe)

> Redakcja serwisu z recenzjami filmowymi codziennie dostaje setki recenzji pisanych przez użytkowników. Żeby pokazać przy filmie, jak przyjęli go widzowie, i szybko wyłapać skrajnie negatywne opinie do moderacji, ktoś musi każdą recenzję przeczytać i oznaczyć jako pozytywną albo negatywną. Przy takiej liczbie tekstów to godziny pracy dziennie, a oceny różnych osób bywają niespójne. System ma na podstawie samego tekstu recenzji wskazać jej wydźwięk (pozytywny / negatywny), żeby redakcja czytała tylko przypadki wątpliwe.

## 4. Dlaczego zwykły algorytm nie wystarczy

- [X] nie umiemy zapisać reguły krok po kroku
- [ ] przepis istnieje, ale jest obliczeniowo za drogi
- [ ] reguł jest za dużo i zmieniają się w czasie

Uzasadnienie (2–3 zdania): Człowiek od razu rozpoznaje, czy recenzja jest pochwałą, czy krytyką, ale nie potrafi tego zapisać jako reguły. Te same słowa zmieniają znaczenie w kontekście („nie był wcale zły”, „tak zły, że aż dobry”), recenzenci używają ironii, a lista „dobrych” i „złych” słów myli się przy zaprzeczeniach i porównaniach. Wiedza o tym, co oznacza pozytywną recenzję, siedzi w oznaczonych przykładach, a nie w regułach.

## 5. Technologia SI (obowiązkowe)

- [ ] sieć neuronowa
- [ ] system ekspertowy / wnioskowanie regułowe
- [ ] algorytm genetyczny
- [X] klasyczne uczenie maszynowe

Dlaczego ta technologia pasuje do tego problemu (2–3 zdania): Problem to klasyfikacja: mamy tysiące recenzji z gotowymi etykietami (pozytywna / negatywna), a reguły rozpoznającej wydźwięk nie umiemy zapisać. Dlatego zamiast pisać reguły pokazujemy systemowi przykłady i pozwalamy mu nauczyć się, które słowa świadczą o recenzji pozytywnej, a które o negatywnej.

## 6. Dane (obowiązkowe)

|||
|---|---|
| Źródło (link do konkretnego zbioru, nie do serwisu) | https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews?resource=download |
| Rozmiar i format | 49582 opinii, w tym 24698 negatywnych i 24698 pozytywnych (pół na pół). Opinie w języku angielskim o różnej długości (najkrótsza 6 słow, najdłuższa 2473 słów, a średnio 231 słów w tym 1287 znaki). W datasecie znajdują się znaczniki html, dlatego konieczne jest wstępne oczyszczenie.|
| Czy dane są już dostępne? | tak |
| Jeśli nie — plan pozyskania | --- |

## 7. Stos technologiczny

```
Wstępne założenia:
- Python 3
- pandas
- scikit-learn
```

## 8. Kryterium sukcesu (obowiązkowe)

- **Metryka:** trafność, czyli procent recenzji z części testowej, którym system przypisał właściwą etykietę (pozytywna / negatywna). Do tego macierz pomyłek: tabela, która pokazuje, ile recenzji pozytywnych system uznał za negatywne i odwrotnie.
- **Próg (liczba):** trafność własnego modelu **co najmniej 80%** na części testowej,
- **Punkt odniesienia** (prosta metoda, z którą porównacie wynik):
    - zawsze najczęstsza klasa: ok. 50%, bo po wyrównaniu w danych jest tyle samo recenzji pozytywnych co negatywnych,
	- prosta lista słów kluczowych: ręcznie spisane polskie słowa pozytywne („świetny”, „znakomity”…) i negatywne („nuda”, „rozczarowanie”…) razem z ich najczęstszymi odmianami („świetny”, „świetna”, „świetne”). System liczy, których słów jest w recenzji więcej, i według tego przypisuje etykietę. Przy remisie wybiera najczęstszą klasę. Listę piszemy, zanim zajrzymy do części testowej.

## 9. Zakres minimalny (obowiązkowe)
```
1. Pozyskanie i przygotowanie danych
- Pobranie surowego zbioru danych z recenzjami filmowymi.
- Konwersja i normalizacja danych do formatu CSV.
- Wybór wymaganych kolumn (review, sentiment).
- Usunięcie duplikatów.
- Usunięcie pustych i niepoprawnych recenzji.
- Uwzględnienie wyłącznie recenzji pozytywnych (2) i negatywnych (0) do treningowego datasetu.
- Zbalansowanie zbioru danych – taka sama liczba recenzji pozytywnych i negatywnych.
- Podział zbioru na:
  - 75% – zbiór treningowy (Training Dataset).
  - 25% – zbiór walidacyjny (Validation Dataset).
- Wyodrębnienie recenzji nieoznaczonych (-1) do zbioru demonstracyjnego (Demo Dataset).
- Eksport przygotowanych zbiorów do osobnych podkatalogów i plików CSV.

2. Przygotowanie prototypu
- Przygotowanie środowiska w Google Colab.
- Wczytanie zbioru danych.
- Przygotowanie reprezentacji cech (Feature).
- Przygotowanie etykiet klas (Labels).
- Implementacja procesu wektoryzacji tekstu przy użyciu TF-IDF.
- Implementacja procesu treningowego.
- Test różnych algorytmów.
- Przygotowanie pierwszego prototypu klasyfikatora sentymentu.
- Weryfikacja poprawności procesu uczenia i predykcji na datasecie walidacyjnym.

3. Dostarczenie działającej aplikacji

4. Porównanie z wcześniej zapisanymi krytariami sukcesu.
```

## 10. Zakres opcjonalny

> TODO
> 
> Co dorobicie, jeśli starczy czasu.

## 11. Repozytorium

Link: https://github.com/gilberthelwich/ml-sentiment-analysis-project

> Raporty sprintów: plik `sprints.txt` w głównym katalogu repozytorium.

## 12. Główne ryzyko i plan awaryjny (obowiązkowe)

**Ryzyko 1: przeciek danych.** Jeśli ta sama recenzja trafi do części uczącej i testowej, wynik będzie fałszywie dobry. _Plan:_ podział na część uczącą i testową ustalamy raz i więcej go nie zmieniamy.

**Ryzyko 2: własny model nie działa poprawnie** _Plan:_ najpierw sprawdzamy jego działanie na próbce 25% danych z datasetu i porównujemy skuteczność do punktu odniesienia. W razie potrzeby dostrajamy parametry.

**Ryzyko 3: inne teksty niż w opisie problemu.** W zbiorze są długie recenzje krytyków i blogerów, a recenzje użytkowników są zwykle krótsze. _Plan:_ opisujemy to w dokumentacji jako ograniczenie. Jeśli starczy czasu, sprawdzamy system na krótkich recenzjach.

---

## Decyzja prowadzącego

> Wypełnia prowadzący — nie edytujcie tej sekcji.

- [ ] zatwierdzony
- [ ] do poprawy

**Uwagi:**

---
*Bartosz Lewandowski · bartosz.lewandowski@cdv.pl · Sztuczna inteligencja — laboratorium · Collegium Da Vinci · rok akad. 2026/2027*
