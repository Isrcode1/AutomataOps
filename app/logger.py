import logging
import os
from dotenv import load_dotenv

load_dotenv()


def setup_logger():
    os.makedirs("logs", exist_ok=True)

    log_level = os.getenv("LOG_LEVEL", "INFO")

    logging.basicConfig(
        filename="logs/engine.log",
        level=getattr(logging, log_level),
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    logging.info("Logger initialized successfully.")
