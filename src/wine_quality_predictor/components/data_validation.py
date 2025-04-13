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
        try:
            file = str(self.config.unzip_data_path)
            if file.endswith(".csv"):
                
                df = pd.read_csv(file)
                df.columns = df.columns.str.strip()  # Strips leading and trailing spaces from column names
                for col, expected_type in self.schema["columns"].items():
                    # print("standing outside loop")
                    print("standing outside loop")
                    print("came out brooooo")
                    if df[col].dtype == expected_type:
                        print("reaced inside loop")
                        logger.warning(f"Data type mismatch: Column '{col}' in {file} has incorrect data type.")
                        return False
                    print("")
            logger.info("All columns have correct data types.")
            return True
        except KeyError as e:
                    logger.error(f"Column '{col}' is missing from the CSV file: {e}")
                    return False
        except Exception as e:
            logger.error(f"Data type validation error: {e}")
            return False

    # def validate_duplicates(self) -> bool:
    #     # """
    #     # Checks for any duplicate rows in the dataset.
    #     # """
    #     # try:
    #     #     file = str(self.config.unzip_data_path)
    #     #     if file.endswith(".csv"):
    #     #         df = pd.read_csv(file)
    #     #         if df.duplicated().any():
    #     #             logger.warning(f"Duplicates found in {file}")
    #     #             return False
    #     #     logger.info("No duplicate rows found.")
    #     #     return True
    #     # except Exception as e:
    #     #     logger.error(f"Duplicate validation error: {e}")
    #     #     return False
    #     return True

    def remove_outliers_iqr(self,df: pd.DataFrame, columns: list) -> pd.DataFrame:
        for col in columns:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR

            original_size = df.shape[0]
            df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
            logger.info(f"Removed outliers from {col}: {original_size - df.shape[0]} rows removed.")

        return df


    def save_validation_status(self, status: bool):
        with open(self.config.STATUS_FILE, 'w') as f:
            f.write(f"Validation status: {status}")
        logger.info(f"Validation status saved to {self.config.STATUS_FILE}")
