from src.wine_quality_predictor.config.configuration import ConfigurationManager
from src.wine_quality_predictor.components.data_transformation import DataTransformation
from src.wine_quality_predictor import logger

STAGE_NAME = "Data Transformation"

def main():
    try:
        logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
        config = ConfigurationManager().get_data_transformation_config()
        transformer = DataTransformation(config)
        transformer.transform_and_split()
        logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n")
    except Exception as e:
        logger.exception(f"Error in stage {STAGE_NAME}: {e}")
        raise e