import os
import subprocess
import zipfile
from wine_quality_predictor.utils.common import get_file_size
import logging
from wine_quality_predictor.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        if not os.path.exists(self.config.local_data_file):
            logging.info("Downloading dataset from Kaggle...")
            command = [
                "kaggle", "datasets", "download",
                "-d", self.config.kaggle_dataset,
                "-p", str(self.config.root_dir),
                "--force"
            ]
            subprocess.run(command, check=True)
            logging.info(f"Downloaded dataset to {self.config.local_data_file}")
        else:
            logging.info("Dataset already downloaded.")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)

        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

        logging.info(f"Extracted zip file to: {unzip_path}")
        logging.info(f"Files extracted: {os.listdir(unzip_path)}")