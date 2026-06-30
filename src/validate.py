from logger import logger


def validate_data(df):
    """
    Validate dataset before transformation.
    """

    logger.info("Running data validation...")

    # Remove rows with missing customer names
    df = df.dropna(subset=["customer_name"])

    # Remove invalid quantities
    df = df[df["quantity"] > 0]

    # Remove invalid prices
    df = df[df["unit_price"] > 0]

    logger.info(f"Validation complete. Records remaining: {len(df)}")

    return df