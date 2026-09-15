import pandas as pd
import sqlite3

df = pd.read_csv("data/processed/aviation_clean.csv")

connection = sqlite3.connect("data/processed/aviation.db")

df.to_sql(
    "aviation",
    connection,
    if_exists="replace",
    index=False
)

connection.close()

print("Database created successfully.")
