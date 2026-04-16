import logging
import os

from app.config import LOG_LEVEL, LOGS_FOLDER, LOG_FILE


def setup_logger():
    os.makedirs(LOGS_FOLDER, exist_ok=True)

    logger = logging.getLogger()
    logger.setLevel(getattr(logging, LOG_LEVEL, logging.INFO))

    if logger.handlers:
        logger.handlers.clear()

    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(getattr(logging, LOG_LEVEL, logging.INFO))

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logging.info("Logger initialized successfully.")
