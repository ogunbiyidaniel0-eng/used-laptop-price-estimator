
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
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
# 4. SAVE TEST DATA FOR MODEL EVALUATION
# ==========================================

evaluation_data = X_test.copy()
evaluation_data["Price (NGN)"] = y_test

evaluation_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "dataset",
        "evaluation_test_data.csv"
    )
)

evaluation_data.to_csv(evaluation_path, index=False)

print("\nEvaluation test data saved successfully!")


# ==========================================
# 5. DISPLAY DATASET INFORMATION
# ==========================================

print("\nDataset preparation completed!")

print("\nTraining data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)

print("\nTraining target shape:", y_train.shape)
print("Testing target shape:", y_test.shape)


# ==========================================
# 6. BUILD PREPROCESSING PIPELINE
# ==========================================

categorical_features = [
    "Brand",
    "Processor_Family",
    "Generation_Category",
    "Condition",
    "Model_Family"
]

numerical_features = [
    "Generation_Number",
    "RAM_GB",
    "HDD_GB",
    "SSD_GB"
]

# Handle missing numerical values
numerical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median"))
])

# Handle categorical values
categorical_transformer = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

# Combine both preprocessing steps
preprocessor = ColumnTransformer(transformers=[
    ("num", numerical_transformer, numerical_features),
    ("cat", categorical_transformer, categorical_features)
])

print("\nPreprocessing pipeline created successfully!")


# ==========================================
# 7. INITIALISE MACHINE LEARNING ALGORITHMS
# ==========================================

models = {
    "Linear Regression": LinearRegression(),

    "Decision Tree": DecisionTreeRegressor(
        max_depth=8,
        random_state=42
    ),

    "Random Forest": RandomForestRegressor(
        n_estimators=200,
        max_depth=12,
        min_samples_leaf=2,
        random_state=42
    )
}

print("\nMachine learning algorithms initialised successfully!")

for model_name in models:
    print(model_name)


# ==========================================
# 8. TRAIN MACHINE LEARNING MODELS
# ==========================================

trained_models = {}

for model_name, model in models.items():

    # Combine preprocessing and model
    pipeline = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ])

    # Train the model
    pipeline.fit(X_train, y_train)

    trained_models[model_name] = pipeline

    print(f"{model_name} trained successfully!")

print("\nAll machine learning models have been trained!")


# ==========================================
# 9. SAVE TRAINED MODELS
# ==========================================

models_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "models"
    )
)

os.makedirs(models_path, exist_ok=True)

for model_name, pipeline in trained_models.items():

    filename = model_name.lower().replace(" ", "_") + ".pkl"

    save_path = os.path.join(models_path, filename)

    joblib.dump(pipeline, save_path)

    print(f"{model_name} saved successfully!")

print("\nAll trained models saved successfully!")
