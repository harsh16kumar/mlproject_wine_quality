from src.wine_quality_predictor.config.configuration import DataTransformationConfig
from src.wine_quality_predictor import logger
from src.wine_quality_predictor.utils.common import make_directory
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import StandardScaler


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def transform_and_split(self):
        logger.info("Reading dataset for transformation and splitting...")
        df = pd.read_csv(self.config.data_path)
        # df = pd.read_csv(self.config.data_path , delimiter=";",quotechar='"')

        # if df.isnull().sum().sum() > 0:
        #     logger.warning("Missing values found. Filling with mean...")
        #     df = df.fillna(df.mean())

        logger.info("Splitting data into train and test...")
        train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
        

        # X_train = train_df.drop("quality", axis=1)
        # y_train = train_df["quality"]
        # X_test = test_df.drop("quality", axis=1)
        # y_test = test_df["quality"]

        # logger.info("Fitting scaler on training data and transforming...")
        # scaler = StandardScaler()
        # X_train_scaled = scaler.fit_transform(X_train)
        # X_test_scaled = scaler.transform(X_test)
        # # X_train_scaled = X_train
        # # X_test_scaled = X_test

        # train_scaled = pd.DataFrame(X_train_scaled, columns=X_train.columns)
        # train_scaled["quality"] = y_train.reset_index(drop=True)

        # test_scaled = pd.DataFrame(X_test_scaled, columns=X_test.columns)
        # test_scaled["quality"] = y_test.reset_index(drop=True)

        logger.info("Creating output directories and saving files...")
        make_directory(self.config.root_dir)

        train_path = self.config.root_dir / "train.csv"
        test_path = self.config.root_dir / "test.csv"

        train_df.to_csv(train_path, index=False)
        train_df.to_csv(test_path, index=False)
        # train_scaled.to_csv(train_path, index=False)
        # test_scaled.to_csv(test_path, index=False)

        # save_bin(self.config.scaler_path, scaler)

        logger.info(f"Train and test data saved to {self.config.root_dir}")
        logger.info(f"Scaler saved at {self.config.scaler_path}")