from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error, r2_score
from src.wine_quality_predictor.config.configuration import ModelTrainerConfig
from src.wine_quality_predictor import logger
from src.wine_quality_predictor.utils.common import make_directory, save_bin
import pandas as pd
from src.wine_quality_predictor.constants import *
# from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        logger.info("Reading training and testing data...")
        train_df = pd.read_csv(self.config.train_data_path)
        test_df = pd.read_csv(self.config.test_data_path)

        X_train = train_df.drop("quality", axis=1)
        y_train = train_df["quality"]
        X_test = test_df.drop("quality", axis=1)
        y_test = test_df["quality"]
        # print(y_train.isna().sum())
        #############################################################
        # logger.info("Training ElasticNet model...")
        # model = ElasticNet(alpha=0.2, l1_ratio=0.1, random_state=42)
        #############################################################
        # logger.info("Training Random Forest Regressor model...")
        # model = RandomForestRegressor(n_estimators=100, random_state=42)
        #############################################################
        logger.info("Training XGBoost Regressor model...")
        model = XGBRegressor(objective='reg:squarederror', n_estimators=100, learning_rate=0.1, max_depth=6, random_state=42)
        #############################################################
        model.fit(X_train, y_train)

        logger.info("Evaluating model...")
        predictions = model.predict(X_test)
        mse = mean_squared_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)

        logger.info(f"Model MSE: {mse:.4f}")
        logger.info(f"Model R^2 Score: {r2:.4f}")

        logger.info("Saving model...")
        make_directory(self.config.root_dir)
        save_bin(self.config.model_path, model)
        logger.info(f"Model saved to: {self.config.model_path}")
        ##lets see accuracy
        print(f"Accuracy: {r2*100:.2f}%")
