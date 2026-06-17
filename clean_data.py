import pandas as pd

df = pd.read_csv("data/Combined Data.csv")

df = df.dropna()
df = df.drop_duplicates()

df.to_csv("data/cleaned_data.csv", index=False)

print("Cleaning Completed")