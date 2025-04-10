from wine_quality_predictor.pipeline.ingestion_pipeline import main as data_ingestion_stage
from wine_quality_predictor.pipeline.validation_pipeline import main as data_validation_stage

if __name__ == "__main__":
    data_ingestion_stage()
    data_validation_stage()
