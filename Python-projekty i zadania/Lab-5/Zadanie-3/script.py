import pandas as pd

df = pd.read_csv(
    "../demografia.csv",
    decimal=",",
    na_values=["", "NA", "brak"]
)
rok_max = df.drop(columns=["KRAJE"]).max().idxmax()
indeks_kraju = df[rok_max].idxmax()
kraj_max = df.loc[indeks_kraju, "KRAJE"]

print(f"Kraj z największym przyrostem ludności: {kraj_max}, rok: {rok_max}")
