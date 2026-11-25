import pandas as pd
import os
from sklearn.model_selection import train_test_split


# ==========================================
# 1. LOAD PROCESSED DATASET
# ==========================================

file_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "dataset",
        "processed_laptops.csv"
    )
)

df = pd.read_csv(file_path)

print("Processed dataset loaded successfully!")


# ==========================================
# 2. SELECT INPUT FEATURES AND TARGET
# ==========================================

features = [
    "Brand",
    "Processor_Family",
    "Generation_Category",
    "Generation_Number",
    "RAM_GB",
    "HDD_GB",
    "SSD_GB",
    "Condition",
    "Model_Family"
]

X = df[features]

y = df["Price (NGN)"]


# ==========================================
# 3. SPLIT DATASET
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# ==========================================
# 4. DISPLAY DATASET INFORMATION
# ==========================================

print("\nDataset preparation completed!")

print("\nTraining data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)

print("\nTraining target shape:", y_train.shape)
print("Testing target shape:", y_test.shape)