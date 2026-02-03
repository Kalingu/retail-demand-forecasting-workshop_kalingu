from src.data_preprocessing import preprocess_run
from src.feature_engineering import add_features, prepare_features
from src.train_model import train_model
from src.evaluate_model import evaluate_model
from src.run_inference_future_predict import run_inference_future_predict
from src.config.config import (
    MODEL_PATH,
    INFERENCE_INPUT_PATH,
    INFERENCE_OUTPUT_PATH,
)
from src.utils.logger import get_logger

logger = get_logger("RetailForecastPipeline")

def main():
    logger.info("Starting Retail Demand Forecasting Pipeline")

    # Step 1: Preprocess data
    df = preprocess_run()
    logger.info("Data loading and preprocessing completed")

    # Step 2: Feature engineering
    df = add_features(df)
    logger.info("Feature engineering completed")
    logger.debug(f"Columns after feature engineering: {df.columns.tolist()}")

    # Step 3: Prepare features for modeling
    x_train, x_test, y_train, y_test = prepare_features(df)
    logger.info("Features prepared & train/test split done")

    # Step 4: Train model
    model = train_model(x_train, y_train, model_path=MODEL_PATH)
    logger.info(f"Model training & saving completed at {MODEL_PATH}")

    # Step 5: Evaluate model
    evaluate_model(model, x_test, y_test)
    logger.info("Model evaluation completed")

    # Step 6: Run Inference
    run_inference_future_predict(
        model_path=MODEL_PATH,
        input_path=INFERENCE_INPUT_PATH,
        output_path=INFERENCE_OUTPUT_PATH
    )
    logger.info("Inference completed & predictions saved")
    logger.info("Pipeline completed successfully")

if __name__ == "__main__":
    main()