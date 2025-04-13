from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    kaggle_dataset: str
    local_data_file: Path
    unzip_dir: Path

@dataclass
class DataValidationConfig:
    root_dir: Path
    unzip_data_path: Path
    STATUS_FILE: Path
    schema_file_path: Path

@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    scaler_path: Path

@dataclass
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_path: Path

@dataclass
class DataVisualizationConfig:
    data_path: Path