# config.py

# Data paths
DATA_RAW_PATH = "data/raw/sales.csv"
DATA_CLEAN_PATH = "data/processed/clean_sales.csv"
DATA_FEATURE_PATH = "data/processed/features.csv"

# Model path
MODEL_PATH = "models/random_forest.pkl"

# Inference paths
INFERENCE_INPUT_PATH = "data/inference/future_data.csv"
INFERENCE_OUTPUT_PATH = "outputs/predictions.csv"

# Features and target
FEATURE_COLS = ["lag_1", "lag_3", "day_of_week"]
TARGET_COL = "sales_qty"
