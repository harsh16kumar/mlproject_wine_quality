from wine_quality_predictor import logger
from wine_quality_predictor.config.configuration import ConfigurationManager
from wine_quality_predictor.components.data_visualization import DataVisualization
import pandas as pd

STAGE_NAME = "Data Visualization"

def main():
    try:
        logger.info(">>>>> Starting Data Visualization stage <<<<<")
        config = ConfigurationManager()
        vis_config = config.get_data_visualization_config()

        visualizer = DataVisualization(config=vis_config)
        visualizer.scatter_plot()
        visualizer.plot_histograms()

        logger.info(">>>>> Data Visualization completed <<<<<\n")

    except Exception as e:
        logger.exception(f"Error in Data Visualization stage: {e}")
        raise e
