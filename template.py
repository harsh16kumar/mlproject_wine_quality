from pathlib import Path
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# List of file paths to create
file_paths = [
    ".github/workflows/ci.yml",
    "config/config.yaml",
    "params.yaml",
    "schema.yaml",
    "templates/index.html",
    "notebooks/eda.ipynb",
    "research/trials.ipynb",
    "tests/test_config.py",
    "tests/test_utils.py",
    "tests/conftest.py",
    "src/mlops_project/__init__.py",
    "src/mlops_project/components/__init__.py",
    "src/mlops_project/components/data_ingestion.py",
    "src/mlops_project/config/__init__.py",
    "src/mlops_project/config/configuration.py",
    "src/mlops_project/constants/__init__.py",
    "src/mlops_project/entity/__init__.py",
    "src/mlops_project/entity/config_entity.py",
    "src/mlops_project/pipeline/__init__.py",
    "src/mlops_project/pipeline/training_pipeline.py",
    "src/mlops_project/utils/__init__.py",
    "src/mlops_project/utils/common.py",
    "src/mlops_project/utils/logger.py",
    "src/mlops_project/monitoring/__init__.py",
    "src/mlops_project/monitoring/drift_detector.py",
    "src/mlops_project/model/model.py",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "README.md",
    ".gitignore",
    ".env"
]

# Create each file and its parent directory
for file_path in file_paths:
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.touch(exist_ok=True)
    logging.info(f"Created file: {file_path}")
