import pandas as pd
df = pd.read_csv(
    "../demografia.csv",
    decimal=",",
    na_values=["", "NA", "brak"]
)
dane_2022 = df["2022"]
print(dane_2022.idxmax())
max_przyrost = dane_2022.idxmax()
kraj = df.loc[max_przyrost, "KRAJE"]
print(f'Kraj, w którym odnotowano największy przyrost ludności to {kraj}')


