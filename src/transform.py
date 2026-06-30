import pandas as pd
from logger import logger


def transform_data(df):
    """
    Clean and transform the sales dataset.
    """

    logger.info("Starting data transformation...")

    # Remove duplicate records
    df = df.drop_duplicates()

    # Remove rows with missing emails
    df = df.dropna(subset=["email"])

    # Convert sale_date to datetime
    df["sale_date"] = pd.to_datetime(df["sale_date"])

    # Standardize product names
    df["product"] = df["product"].str.title()

    # Create total_sales column
    df["total_sales"] = df["quantity"] * df["unit_price"]

    logger.info(f"Transformation complete. Remaining records: {len(df)}")

    return df