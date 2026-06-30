from sqlalchemy import create_engine
from logger import logger
from config import DATABASE_NAME

DATABASE_URL = f"sqlite:///{DATABASE_NAME}"

engine = create_engine(DATABASE_URL)


def get_engine():
    """
    Return SQLAlchemy engine.
    """
    logger.info("Database connection established.")
    return engine