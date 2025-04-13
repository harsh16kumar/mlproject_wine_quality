from wine_quality_predictor.config.configuration import ConfigurationManager
from wine_quality_predictor.components.data_validation import DataValidation
import pandas as pd

from wine_quality_predictor import logger

STAGE_NAME = "Data Validation"

def main():
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        config = ConfigurationManager().get_data_validation_config()
        validation = DataValidation(config)


        df = pd.read_csv(str("artifacts/data_ingestion/unzipped_data/winequality-red.csv") , delimiter=';', quotechar='"')
        columns_to_clean = [
            "chlorides",
            "residual sugar",
            "free sulfur dioxide",
            "total sulfur dioxide"
        ]
        # df_cleaned = validation.remove_outliers_iqr(df, columns_to_clean)

        # Optional: Save cleaned data
        df.to_csv("artifacts/data_ingestion/unzipped_data/winequality-red.csv", index=False)
        logger.info("Saved cleaned data to artifacts/data_ingestion/unzipped_data/winequality-red.csv")
        
        column_status = validation.validate_all_columns()
        null_status = validation.validate_null_values()
        # data_type_status = validation.validate_data_types()
        # duplicate_status = validation.validate_duplicates()

        final_status = column_status and null_status
        validation.save_validation_status(final_status)

        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n")

    except Exception as e:
        logger.exception(f"Error in stage {STAGE_NAME}: {e}")
        raise e
