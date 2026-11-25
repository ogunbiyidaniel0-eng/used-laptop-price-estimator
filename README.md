# Used Laptop Price Estimator

A Machine Learning web application that estimates the resale price of used laptops based on their specifications.

## Live Application

**Try it here:** https://used-laptop-price-estimator.streamlit.app/

## Project Overview

The Used Laptop Price Estimator uses machine learning algorithms to predict the estimated resale value of used laptops in Nigerian Naira (NGN).

Users can provide laptop specifications such as brand, processor, generation, RAM, storage capacity, and condition to receive an estimated price.

## Objectives

- Develop a machine learning system for estimating used laptop prices.
- Compare different regression algorithms.
- Evaluate model performance using appropriate metrics.
- Build an interactive web application for generating predictions.

## Machine Learning Algorithms

Three regression algorithms were trained and evaluated:

1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor

The models were evaluated using:
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score
- Median Percentage Error
- 5-Fold Cross-Validation

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
- Matplotlib
- Seaborn
- Git and GitHub

## Features

- Laptop brand selection
- Laptop model selection
- Processor and generation selection
- RAM and storage specifications
- Laptop condition selection
- Price estimation using trained machine learning models
- Comparison of predictions from different algorithms

## Project Structure

```text
used-laptop-price-estimator/
│
├── dataset/
├── documentation/
├── frontend/
│   └── app.py
├── models/
├── notebooks/
├── presentation/
├── src/
│   ├── check_dataset.py
│   ├── prepare_data.py
│   ├── train_model.py
│   └── evaluate_model.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/ogunbiyidan0-eng/used-laptop-price-estimator.git
```

### 2. Navigate into the project folder

```bash
cd used-laptop-price-estimator
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
streamlit run frontend/app.py
```

## Project Status

The machine learning models have been trained and evaluated, and the web application has been successfully deployed using Streamlit Community Cloud.

## Author

Developed as a group Machine Learning project.