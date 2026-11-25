
import pandas as pd
import os
import re


# ==========================================
# LOAD DATASET
# ==========================================

file_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "dataset",
        "Used_laptop_dataset (1).csv"
    )
)

df = pd.read_csv(file_path)

print("Dataset loaded successfully!")


# ==========================================
# 1. REMOVE DUPLICATE RECORDS
# ==========================================

original_count = len(df)

df = df.drop_duplicates(
    subset=df.columns.drop("ID"),
    keep="first"
)

removed_count = original_count - len(df)

print(f"\nDuplicate records removed: {removed_count}")
print(f"Remaining records: {len(df)}")


# ==========================================
# 2. RAM CONVERSION
# ==========================================

df["RAM_GB"] = df["RAM"].str.extract(r"(\d+)").astype(int)

print("\nRAM conversion:")
print(df[["RAM", "RAM_GB"]].drop_duplicates())


# ==========================================
# 3. STORAGE CONVERSION
# ==========================================

def convert_storage(storage):
    storage = storage.upper()

    # Extract HDD and SSD capacities
    hdd_values = re.findall(r"(\d+)\s*(TB|GB)\s*HDD", storage)
    ssd_values = re.findall(r"(\d+)\s*(TB|GB)\s*SSD", storage)

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
        emmc_values = re.findall(r"(\d+)\s*(TB|GB)", storage)

        for value, unit in emmc_values:
            ssd_gb += int(value) * (1024 if unit == "TB" else 1)

    # Mark unknown SSD capacity as missing
    if re.search(r"HDD\s*\+\s*SSD", storage):
        ssd_gb = float("nan")

    return pd.Series([hdd_gb, ssd_gb])


df[["HDD_GB", "SSD_GB"]] = df["Storage"].apply(convert_storage)

print("\nStorage conversion:")
print(df[["Storage", "HDD_GB", "SSD_GB"]].drop_duplicates())


# ==========================================
# 4. PROCESSOR STANDARDISATION
# ==========================================

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


# ==========================================
# 5. GENERATION STANDARDISATION
# ==========================================

def standardise_generation(generation):
    generation = generation.strip()

    if generation.lower() == "brasswell":
        return "Braswell"

    return generation


df["Generation_Category"] = df["Generation"].apply(standardise_generation)

# Extract Intel generation numbers only
df["Generation_Number"] = (
    df["Generation_Category"]
    .where(df["Generation_Category"].str.contains("Gen", case=False))
    .str.extract(r"(\d+)")
    .astype(float)
)

print("\nStandardised generations:")
print(
    df[
        ["Generation", "Generation_Category", "Generation_Number"]
    ].drop_duplicates()
)


# ==========================================
# 6. LAPTOP MODEL FAMILY STANDARDISATION
# ==========================================

def standardise_model(row):
    brand = row["Brand"].lower()
    model = row["Model"].lower()

    if brand == "hp":
        families = {
            "elitebook": "EliteBook",
            "chromebook": "Chromebook",
            "probook": "ProBook",
            "zbook": "ZBook",
            "pavilion": "Pavilion",
            "omen": "Omen",
            "envy": "Envy",
            "spectre": "Spectre"
        }

    elif brand == "dell":
        families = {
            "latitude": "Latitude",
            "inspiron": "Inspiron"
        }

    elif brand == "lenovo":
        families = {
            "thinkpad": "ThinkPad",
            "ideapad": "IdeaPad",
            "yoga": "Yoga"
        }

    elif brand == "apple":
        families = {
            "macbook pro": "MacBook Pro",
            "macbook air": "MacBook Air"
        }

    elif brand == "asus":
        families = {
            "vivobook": "VivoBook",
            "zenbook": "ZenBook",
            "tuf": "TUF Gaming",
            "rog": "ROG"
        }

    elif brand == "acer":
        families = {
            "aspire": "Aspire",
            "travelmate": "TravelMate",
            "swift": "Swift",
            "nitro": "Nitro",
            "predator": "Predator"
        }

    elif brand == "msi":
        families = {
            "gf": "MSI Gaming",
            "ge": "MSI Gaming",
            "gs": "MSI Gaming",
            "gp": "MSI Gaming",
            "sword": "Sword",
            "stealth": "Stealth",
            "pulse": "Pulse",
            "katana": "Katana"
        }

    elif brand == "toshiba":
        families = {
            "satellite": "Satellite",
            "portege": "Portege",
            "dynabook satellite": "Satellite"
        }

    else:
        families = {}

    for prefix, family in families.items():
        if model.startswith(prefix):
            return family

    return "Other"


df["Model_Family"] = df.apply(standardise_model, axis=1)

print("\nStandardised laptop model families:")
print(
    df[["Brand", "Model", "Model_Family"]].drop_duplicates()
)

print("\nModel family counts:")
print(df["Model_Family"].value_counts())


# ==========================================
# 7. DATASET SUMMARY
# ==========================================

print("\nFinal dataset shape:")
print(df.shape)

print("\nNew feature columns:")
print([
    "RAM_GB",
    "HDD_GB",
    "SSD_GB",
    "Processor_Family",
    "Generation_Category",
    "Generation_Number",
    "Model_Family"
])

print("\nFeature engineering completed successfully!")


# ==========================================
# 8. FEATURE ENGINEERING QUALITY CHECK
# ==========================================

print("\nMissing values after feature engineering:")
print(df.isnull().sum())

print("\nDuplicate records (excluding ID):")
print(df.drop(columns=["ID"]).duplicated().sum())

print("\nStorage values requiring review:")
print(
    df[df["Storage"].str.contains(r"HDD\s*\+\s*SSD", case=False)][
        ["Storage", "HDD_GB", "SSD_GB"]
    ]
)

print("\nModel families classified as Other:")
print(df[df["Model_Family"] == "Other"][["Brand", "Model"]])
# ==========================================
# 9. SAVE PROCESSED DATASET
# ==========================================

output_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "dataset",
        "processed_laptops.csv"
    )
)

df.to_csv(output_path, index=False)

print("\nProcessed dataset saved successfully!")
print(f"Saved to: {output_path}")