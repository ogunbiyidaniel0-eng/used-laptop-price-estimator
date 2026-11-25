
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



import re

def convert_storage(storage):
    storage = storage.upper()

    # Extract HDD and SSD capacities
    hdd_values = re.findall(r'(\d+)\s*(TB|GB)\s*HDD', storage)
    ssd_values = re.findall(r'(\d+)\s*(TB|GB)\s*SSD', storage)

    hdd_gb = sum(
        int(value) * (1024 if unit == "TB" else 1)
        for value, unit in hdd_values
    )

    ssd_gb = sum(
        int(value) * (1024 if unit == "TB" else 1)
        for value, unit in ssd_values
    )

    # Handle eMMC storage
    if "EMMC" in storage:
        emmc_values = re.findall(r'(\d+)\s*(TB|GB)', storage)
        for value, unit in emmc_values:
            ssd_gb += int(value) * (1024 if unit == "TB" else 1)

    return pd.Series([hdd_gb, ssd_gb])


df[["HDD_GB", "SSD_GB"]] = df["Storage"].apply(convert_storage)

print("\nStorage conversion:")
print(df[["Storage", "HDD_GB", "SSD_GB"]].head(20))

def standardise_processor(processor):
    processor = processor.strip()

    if "Apple M1 Pro" in processor:
        return "Apple M1 Pro"
    elif "Apple M1" in processor:
        return "Apple M1"
    elif "Apple M2" in processor:
        return "Apple M2"
    elif "Intel Core i3" in processor:
        return "Intel Core i3"
    elif "Intel Core i5" in processor:
        return "Intel Core i5"
    elif "Intel Core i7" in processor:
        return "Intel Core i7"
    elif "Intel Core i9" in processor:
        return "Intel Core i9"
    elif "Intel Celeron" in processor:
        return "Intel Celeron"
    elif "Intel Pentium" in processor:
        return "Intel Pentium"
    elif "AMD Ryzen 3" in processor:
        return "AMD Ryzen 3"
    elif "AMD Ryzen 5" in processor:
        return "AMD Ryzen 5"
    elif "AMD Ryzen 7" in processor:
        return "AMD Ryzen 7"
    elif "AMD Ryzen 9" in processor:
        return "AMD Ryzen 9"
    elif "AMD A4" in processor:
        return "AMD A4"
    else:
        return "Other"


df["Processor_Family"] = df["Processor"].apply(standardise_processor)

print("\nStandardised processor categories:")
print(df[["Processor", "Processor_Family"]].drop_duplicates())


print("\nProcessor values:")
print(df["Processor"].unique())