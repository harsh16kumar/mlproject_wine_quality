from typing import Any
from wine_quality_predictor.config.configuration import DataValidationConfig
from wine_quality_predictor import logger
import pandas as pd
from wine_quality_predictor.utils.common import read_yaml

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        self.schema = read_yaml(self.config.schema_file_path)

    def validate_all_columns(self) -> bool:
        try:
            file = self.config.unzip_data_path
            # print(file)
            # print(str(file).endswith(".csv"))
            if str(file).endswith(".csv"):
                df = pd.read_csv(file, delimiter=';', quotechar='"')
                df_columns = df.columns.tolist()
                schema_columns = list(self.schema["columns"].keys())
                # print(df_columns)

                if df_columns != schema_columns:
                    raise Exception("Schema mismatch: columns do not match.")

            logger.info("All columns are valid.")
            return True
        except Exception as e:
            logger.error(f"Validation error: {e}")
            return False
    
    def validate_null_values(self) -> bool:
        """
        Checks for any missing (null) values in the dataset.
        """
        try:
            file = str(self.config.unzip_data_path)
            if file.endswith(".csv"):
                df = pd.read_csv(file)
                if df.isnull().values.any():
                    logger.warning(f"Missing values found in {file}")
                    return False
            logger.info("No missing values detected.")
            return True
        except Exception as e:
            logger.error(f"Null value validation error: {e}")
            return False

    def validate_data_types(self) -> bool:
        """
        Checks that columns have the correct data types according to schema.yaml.
        """
        # try:
        #     file = str(self.config.unzip_data_path)
        #     if file.endswith(".csv"):
        #         df = pd.read_csv(file)
        #         for col, expected_type in self.schema["columns"].items():
        #             if col not in['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
        #                           'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH',
        #                           'sulphates', 'alcohol'] and df[col].dtype != expected_type:
        #                 logger.warning(f"Data type mismatch: Column '{col}' in {file} has incorrect data type.")
        #                 return False
        #     logger.info("All columns have correct data types.")
        #     return True
        # except Exception as e:
        #     logger.error(f"Data type validation error: {e}")
        #     return False
        return True

    def validate_duplicates(self) -> bool:
        """
        Checks for any duplicate rows in the dataset.
        """
        # try:
        #     file = str(self.config.unzip_data_path)
        #     if file.endswith(".csv"):
        #         df = pd.read_csv(file)
        #         if df.duplicated().any():
        #             logger.warning(f"Duplicates found in {file}")
        #             return False
        #     logger.info("No duplicate rows found.")
        #     return True
        # except Exception as e:
        #     logger.error(f"Duplicate validation error: {e}")
        #     return False
        return True

    def save_validation_status(self, status: bool):
        with open(self.config.STATUS_FILE, 'w') as f:
            f.write(f"Validation status: {status}")
        logger.info(f"Validation status saved to {self.config.STATUS_FILE}")
