from logger import logger


def print_pipeline_summary(records_before, records_after):
    """
    Display ETL summary.
    """

    logger.info("===================================")
    logger.info("ETL SUMMARY")
    logger.info("===================================")

    logger.info(f"Records Extracted : {records_before}")
    logger.info(f"Records Loaded    : {records_after}")
    logger.info(f"Duplicates Removed: {records_before - records_after}")

    logger.info("===================================")