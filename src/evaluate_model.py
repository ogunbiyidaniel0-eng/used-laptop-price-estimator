from sklearn.model_selection import cross_validate, train_test_split
import os
import joblib
import pandas as pd
import time

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


# ==========================================
# 1. LOAD EVALUATION DATA
# ==========================================

base_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

data_path = os.path.join(
    base_path,
    "dataset",
    "evaluation_test_data.csv"
)

test_data = pd.read_csv(data_path)

X_test = test_data.drop(columns=["Price (NGN)"])
y_test = test_data["Price (NGN)"]

print("Evaluation dataset loaded successfully!")
print("Testing records:", len(test_data))


# ==========================================
# 2. LOAD TRAINED MODELS
# ==========================================

models_path = os.path.join(base_path, "models")

models = {
    "Linear Regression": joblib.load(
        os.path.join(models_path, "linear_regression.pkl")
    ),

    "Decision Tree": joblib.load(
        os.path.join(models_path, "decision_tree.pkl")
    ),

    "Random Forest": joblib.load(
        os.path.join(models_path, "random_forest.pkl")
    )
}

print("\nAll trained models loaded successfully!")


# ==========================================
# 3. TEST AND EVALUATE MODELS
# ==========================================

results = []

for model_name, model in models.items():

    start_time = time.perf_counter()

    predictions = model.predict(X_test)

    prediction_time = time.perf_counter() - start_time

    mae = mean_absolute_error(y_test, predictions)

    rmse = mean_squared_error(
        y_test,
        predictions
    ) ** 0.5

    r2 = r2_score(y_test, predictions)

    percentage_errors = (
        abs(y_test - predictions) / y_test
    ) * 100

    median_percentage_error = percentage_errors.median()

    results.append({
        "Model": model_name,
        "MAE (NGN)": mae,
        "RMSE (NGN)": rmse,
        "R2 Score": r2,
        "Median Percentage Error (%)": median_percentage_error,
        "Prediction Time (seconds)": prediction_time
    })

    print(f"\n{model_name} evaluated successfully!")


# ==========================================
# 4. DISPLAY COMPARISON RESULTS
# ==========================================

results_df = pd.DataFrame(results)

print("\n==========================================")
print("MODEL EVALUATION RESULTS")
print("==========================================")

print(results_df.to_string(index=False))


# ==========================================
# 5. SAVE EVALUATION RESULTS
# ==========================================

output_path = os.path.join(
    base_path,
    "documentation",
    "model_evaluation_results.csv"
)

results_df.to_csv(output_path, index=False)

print("\nEvaluation results saved successfully!")

# ==========================================
# 6. PERFORM 5-FOLD CROSS-VALIDATION
# ==========================================

print("\n==========================================")
print("5-FOLD CROSS-VALIDATION")
print("==========================================")

# Load the original training data
processed_data_path = os.path.join(
    base_path,
    "dataset",
    "processed_laptops.csv"
)

processed_data = pd.read_csv(processed_data_path)

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

X = processed_data[features]
y = processed_data["Price (NGN)"]

# Recreate the same training split
X_train, _, y_train, _ = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Evaluate each model using 5-fold cross-validation
cv_results = []

for model_name, model in models.items():

    scores = cross_validate(
        model,
        X_train,
        y_train,
        cv=5,
        scoring={
            "mae": "neg_mean_absolute_error",
            "r2": "r2"
        }
    )

    mean_mae = -scores["test_mae"].mean()
    mean_r2 = scores["test_r2"].mean()

    cv_results.append({
        "Model": model_name,
        "Mean MAE (NGN)": mean_mae,
        "Mean R2 Score": mean_r2
    })

    print(f"\n{model_name}")
    print(f"Mean MAE: ₦{mean_mae:,.2f}")
    print(f"Mean R2 Score: {mean_r2:.4f}")


# Save cross-validation results
cv_results_df = pd.DataFrame(cv_results)

cv_output_path = os.path.join(
    base_path,
    "documentation",
    "cross_validation_results.csv"
)

cv_results_df.to_csv(cv_output_path, index=False)

print("\nCross-validation results saved successfully!")
# ==========================================
# 7. INSPECT INDIVIDUAL MODEL PREDICTIONS
# ==========================================

print("\n==========================================")
print("INDIVIDUAL PREDICTION INSPECTION")
print("==========================================")

prediction_results = pd.DataFrame({
    "Actual Price (NGN)": y_test.values
})

for model_name in ["Linear Regression", "Random Forest"]:

    predictions = models[model_name].predict(X_test)

    prediction_results[f"{model_name} Prediction"] = predictions

    prediction_results[f"{model_name} Absolute Error"] = (
        abs(y_test.values - predictions)
    )

print("\nFirst 10 prediction comparisons:")
print(prediction_results.head(10).to_string(index=False))

# Save prediction inspection results
inspection_path = os.path.join(
    base_path,
    "documentation",
    "prediction_inspection.csv"
)

prediction_results.to_csv(inspection_path, index=False)

print("\nPrediction inspection results saved successfully!")