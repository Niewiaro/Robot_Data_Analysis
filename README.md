# Robot Data Analysis

AGH 🟩⬛🟥

Projekt na zajęcia "Roboty Przemysłowe" na AGH, napisany w Pythonie.

## Spis Treści

- [Opis](#opis)
- [Wymagania](#wymagania)
- [Instalacja](#instalacja)
- [Użycie](#użycie)
  - [Konwersja danych](#konwersja-danych)
  - [Import danych](#import-danych)
  - [Tworzenie wykresu](#tworzenie-wykresu)
  - [Oczyszczenie danych z błędów pomiarowych](#oczyszczenie-danych-z-błędów-pomiarowych)
  - [Oczyszczony wykres](#oczyszczony-wykres)
- [Autor](#autor)
- [Licencja](#licencja)

## Opis

Ten projekt obejmuje analizę danych z czujników robota. Dane są przekształcane, wizualizowane i oczyszczane z błędów pomiarowych.

## Wymagania

- Python 3.x
- Pandas
- Matplotlib

## Instalacja

1. Sklonuj repozytorium:
    ```sh
    git clone https://github.com/Niewiaro/Robot_Data_Analysis.git
    cd Robot_Data_Analysis
    ```

2. Zainstaluj wymagane biblioteki:
    ```sh
    pip install pandas matplotlib
    ```

## Użycie

### Konwersja danych

Aby skonwertować plik tekstowy na plik CSV:

```python
from converter import convert_txt_to_csv

convert_txt_to_csv("data", "data")
```

### Import danych

Aby zaimportować dane do DataFrame:

```python
import pandas as pd

file_path = 'data.csv'
df = pd.read_csv(file_path, names=['z_V', 'y_V', 'x_V'])

samples_rate = 500  # czas próbkowania w Hz
df['t_s'] = df.index / samples_rate  # 500 Hz = 0.002s

df['z_mm'] = df['z_V'] / 0.1
df['y_mm'] = df['y_V'] / 0.143
df['x_mm'] = df['x_V'] / 0.143
```

### Tworzenie wykresu

Aby stworzyć wykres z danych:

```python
import matplotlib.pyplot as plt

scale = 15
fig = plt.figure(figsize=(297/scale, 210/scale))  # 297mm x 210mm (A4 poziomo)

plt.plot(df['t_s'], df['x_mm'], label='x_mm')
plt.plot(df['t_s'], df['y_mm'], label='y_mm')
plt.plot(df['t_s'], df['z_mm'], label='z_mm')

plt.xlabel('Czas [s]')
plt.ylabel('Przemieszczenie [mm]')
plt.title('Wykres liniowy dla osi x, y i z w przebiegu czasowym')
plt.legend()

plt.savefig('wykres_mm.svg', format='svg', dpi=800)
plt.show()
```

### Oczyszczenie danych z błędów pomiarowych

Aby oczyścić dane z błędów pomiarowych:

```python
threshold = 0.1

diff_x = df['x_mm'].diff().abs()
diff_y = df['y_mm'].diff().abs()
diff_z = df['z_mm'].diff().abs()

to_remove = (diff_x > threshold) | (diff_y > threshold) | (diff_z > threshold)

df_cleaned = df[~to_remove]
```

### Oczyszczony wykres

Aby stworzyć wykres z oczyszczonych danych:

```python
fig = plt.figure(figsize=(297/scale, 210/scale))

plt.plot(df_cleaned['t_s'], df_cleaned['x_mm'], label='x_mm')
plt.plot(df_cleaned['t_s'], df_cleaned['y_mm'], label='y_mm')
plt.plot(df_cleaned['t_s'], df_cleaned['z_mm'], label='z_mm')

plt.xlabel('Czas [s]')
plt.ylabel('Przemieszczenie [mm]')
plt.title('Wykres liniowy dla osi x, y i z w przebiegu czasowym - oczyszczone dane')
plt.legend()

plt.savefig('wykres_cleaned_mm.svg', format='svg', dpi=800)
plt.show()
```

## Autor

Jakub Niewiarowski

## Licencja

Ten projekt jest licencjonowany na zasadach licencji MIT. Szczegóły w pliku [LICENSE](LICENSE).
