import glob
import pandas as pd

files = glob.glob("data/raw/table09_*.csv")

print(len(files))

df = pd.read_csv(files[0])

print(df.head())
print(df.columns)

column_counts = []

for file in files:
    df = pd.read_csv(file)
    column_counts.append(len(df.columns))

print(set(column_counts))

all_data = []

for file in files:
    df = pd.read_csv(file)
    all_data.append(df)

combined_df = pd.concat(all_data, ignore_index=True)

print(combined_df.shape)

combined_df.to_csv(
    "data/processed/table09_combined.csv",
    index=False
)
