import pandas as pd
import os

file_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "dataset", "Used_laptop_dataset (1).csv")
)
df = pd.read_csv(file_path)

print("Dataset loaded successfully!")
print("\nFirst 5 rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())
print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nDataset information:")
df.info()