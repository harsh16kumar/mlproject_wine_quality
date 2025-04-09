import os
import json
import yaml
import joblib
from pathlib import Path
from typing import (Any,Union)
from ensure import ensure_annotations
from box import ConfigBox
from box.exceptions import BoxValueError

from wine_quality_predictor import logger

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    try:
        with open(path, 'r') as f:
            content = json.load(f)
            logger.info(f"Loaded JSON file from: {path}")
            return ConfigBox(content)
    except BoxValueError as e:
        logger.error(f"Error reading JSON file at {path}: {e}")
        raise e
    except Exception as e:
        logger.error(f"Unexpected error reading JSON file at {path}: {e}")
        raise e


@ensure_annotations
def save_json(path: Path, data: dict) -> None:
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
        logger.info(f"Saved JSON file at: {path}")


@ensure_annotations
def read_yaml(path: Path) -> ConfigBox:
    try:
        with open(path,'r') as f:
            content = yaml.safe_load(f)
            logger.info(f"Loaded YAML file from: {path}")
            return ConfigBox(content)
    except BoxValueError as e:
        logger.error(f"BoxValueError while loading YAML at {path}: {e}")
        raise e
    except Exception as e:
        logger.error(f"Error reading YAML file at {path}: {e}")
        raise e


# @ensure_annotations
def make_directory(path: Path, verbose=True) -> None:
    path = Path(path)
    os.makedirs(path, exist_ok=True)
    if verbose:
        logger.info(f"Created directory: {path}")


@ensure_annotations
def save_bin(path: Path, data: Any) -> None:
    joblib.dump(value=data, filename=path)
    logger.info(f"Saved binary file at: {path}")


@ensure_annotations
def read_bin(path: Path) -> Any:
    data = joblib.load(path)
    logger.info(f"Loaded binary file from: {path}")
    return data

@ensure_annotations
def get_file_size(path: Path) -> str:
    size_in_bytes = path.stat().st_size
    size_in_kb = round(size_in_bytes / 1024, 2)
    human_readable = f"{size_in_kb} KB"
    logger.info(f"Size of file {path}: {human_readable}")
    return human_readable
