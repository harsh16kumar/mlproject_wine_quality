from pathlib import Path
from typing import Any, Dict

from wine_quality_predictor.utils.common import read_yaml, make_directory
from wine_quality_predictor.constants import *
from wine_quality_predictor.entity.config_entity import DataIngestionConfig
from wine_quality_predictor import logger


class ConfigurationManager:
    def __init__(
        self,
        config_filepath: Path = CONFIG_FILE_PATH,
        params_filepath: Path = PARAMS_FILE_PATH,
        schema_filepath: Path = SCHEMA_FILE_PATH
    ):
        self.config_filepath = config_filepath
        # self.params_filepath = params_filepath
        # self.schema_filepath = schema_filepath

        self.config = read_yaml(Path(self.config_filepath))
        # self.params = read_yaml(self.params_filepath)
        # self.schema = read_yaml(self.schema_filepath)

        make_directory(Path(self.config.artifacts_root))

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        make_directory(config.root_dir)

        return DataIngestionConfig(
            root_dir=config.root_dir,
            kaggle_dataset=config.kaggle_dataset,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
