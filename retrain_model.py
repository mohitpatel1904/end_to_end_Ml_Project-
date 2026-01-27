"""
Quick script to retrain the model with current sklearn version
"""
import os
import sys
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score
import pickle

# Read data
df = pd.read_csv('notebook/data/stud.csv')
print(f"Data loaded: {df.shape}")

# Define features and target
target = 'math_score'
numerical_columns = ["writing_score", "reading_score"]
categorical_columns = [
    "gender",
    "race_ethnicity",
    "parental_level_of_education",
    "lunch",
    "test_preparation_course",
]

X = df.drop(columns=[target])
y = df[target]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"Train: {X_train.shape}, Test: {X_test.shape}")

# Create preprocessor
num_pipeline = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

cat_pipeline = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("one_hot_encoder", OneHotEncoder(handle_unknown='ignore')),
    ("scaler", StandardScaler(with_mean=False))
])

preprocessor = ColumnTransformer([
    ("num_pipeline", num_pipeline, numerical_columns),
    ("cat_pipelines", cat_pipeline, categorical_columns)
])

# Fit preprocessor and transform data
X_train_transformed = preprocessor.fit_transform(X_train)
X_test_transformed = preprocessor.transform(X_test)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train_transformed, y_train)

# Evaluate
y_pred = model.predict(X_test_transformed)
r2 = r2_score(y_test, y_pred)
print(f"R2 Score: {r2:.4f}")

# Save model and preprocessor
os.makedirs('artifacts', exist_ok=True)

with open('artifacts/model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("Model saved to artifacts/model.pkl")

with open('artifacts/preprocessor.pkl', 'wb') as f:
    pickle.dump(preprocessor, f)
print("Preprocessor saved to artifacts/preprocessor.pkl")

print("\nRetraining complete! You can now run the app.")
