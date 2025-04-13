import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from src.wine_quality_predictor.config.configuration import DataVisualizationConfig
from src.wine_quality_predictor import logger



class DataVisualization:
    def __init__(self, config: DataVisualizationConfig):
        self.config = config

    def load_data(self):
        logger.info(f"Loading data from {self.config.data_path}")
        # return pd.read_csv(self.config.data_path, delimiter=";", quotechar='"')
        return pd.read_csv(self.config.data_path)

    def scatter_plot(self):
        df = self.load_data()
        features = df.columns.drop("quality")
        logger.info("Creating scatter plots...")
        plt.figure(figsize=(16, 12))

        for idx, feature in enumerate(features):
            plt.subplot(4, 3, idx + 1)
            sns.scatterplot(data=df, x=feature, y="quality", alpha=0.6)
            plt.title(f"{feature} vs Quality")
            plt.tight_layout()

        plt.suptitle("Feature vs Target Scatter Plots", fontsize=18, y=1.02)
        plt.show()

    def plot_histograms(self):
        df = self.load_data()
        logger.info("Generating histograms for all features...")
        df.hist(figsize=(15, 10), bins=20, color='skyblue', edgecolor='black')
        plt.tight_layout()
        plt.suptitle("Histogram of All Features", fontsize=16)
        plt.subplots_adjust(top=0.92)
        plt.savefig("artifacts/data_visualization/histograms.png")
        plt.close()
        logger.info("Histogram plot saved at: artifacts/data_visualization/histograms.png")