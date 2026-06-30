import pandas as pd
from logger import logger


def extract_data(file_path):
    """
    Extract data from a CSV file.
    """

    logger.info(f"Reading data from: {file_path}")

    df = pd.read_csv(file_path)

    logger.info(f"{len(df)} records extracted successfully.")

    return df