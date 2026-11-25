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