from logger import logger
from extract import extract_data
from validate import validate_data
from transform import transform_data
from load import load_data
from utils import print_pipeline_summary

logger.info("===================================")
logger.info("Enterprise Sales ETL Pipeline")
logger.info("===================================")

try:

    # Extract
    df = extract_data("data/raw/sales_data.csv")
    extracted_records = len(df)

    # Validate
    df = validate_data(df)

    # Transform
    df = transform_data(df)
    loaded_records = len(df)

    # Load
    load_data(df)

    # Summary
    print_pipeline_summary(extracted_records, loaded_records)

    logger.info("ETL Pipeline completed successfully.")

except Exception as e:
    logger.error(f"Pipeline failed: {e}")