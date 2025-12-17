import pandas as pd

df = pd.read_csv(
    "demografia.csv",
    decimal=",",
    na_values=["", "NA", "brak"]
)

print(df)
