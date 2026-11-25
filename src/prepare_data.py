
import pandas as pd
import os

file_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "dataset", "Used_laptop_dataset (1).csv")
)

df = pd.read_csv(file_path)

# Convert RAM values into numbers
df["RAM_GB"] = df["RAM"].str.extract(r"(\d+)").astype(int)

print("Original RAM values:")
print(df["RAM"].unique())

print("\nConverted RAM values:")
print(df[["RAM", "RAM_GB"]].head(10))
