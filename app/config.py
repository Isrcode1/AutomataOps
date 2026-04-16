import os
from dotenv import load_dotenv

load_dotenv()

TASKS_FOLDER = os.getenv("TASKS_FOLDER", "tasks/pending")
COMPLETED_FOLDER = os.getenv("COMPLETED_FOLDER", "tasks/completed")
FAILED_FOLDER = os.getenv("FAILED_FOLDER", "tasks/failed")

LOGS_FOLDER = os.getenv("LOGS_FOLDER", "logs")
LOG_FILE = os.getenv("LOG_FILE", os.path.join(LOGS_FOLDER, "engine.log"))
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()
