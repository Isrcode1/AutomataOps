import logging
import os

from app.config import LOG_LEVEL, LOGS_FOLDER, LOG_FILE


def setup_logger():
    os.makedirs(LOGS_FOLDER, exist_ok=True)

    logging.basicConfig(
        filename=LOG_FILE,
        level=getattr(logging, LOG_LEVEL.upper(), logging.INFO),
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    logging.info("Logger initialized successfully.")
