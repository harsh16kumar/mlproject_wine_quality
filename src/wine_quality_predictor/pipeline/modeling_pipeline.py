from src.wine_quality_predictor.config.configuration import ConfigurationManager
from src.wine_quality_predictor.components.data_modeling import ModelTrainer
from src.wine_quality_predictor import logger
from src.wine_quality_predictor.utils.common import make_directory, save_bin
import pandas as pd

STAGE_NAME = "Model Training"

def main():
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        config = ConfigurationManager().get_model_trainer_config()
        trainer = ModelTrainer(config)
        trainer.train()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n")
    except Exception as e:
        logger.exception(f"Error in stage {STAGE_NAME}: {e}")
        raise e