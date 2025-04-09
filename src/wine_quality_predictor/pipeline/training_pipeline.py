from src.wine_quality_predictor.config.configuration import ConfigurationManager
from src.wine_quality_predictor.components.data_ingestion import DataIngestion
import logging

STAGE_NAME = "Data Ingestion"

def main():
    try:
        logging.info(f">>>>>> Stage Data Ingestion started <<<<<<")
        
        data_ingestion_config = ConfigurationManager()
        config = data_ingestion_config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config)
        data_ingestion.download_data()
        data_ingestion.extract_zip_file()

        logging.info(f">>>>>> Stage Data Ingestion completed <<<<<<\n")

    except Exception as e:
        logging.exception(f"Error occurred in stage {STAGE_NAME}: {e}")
        raise e
