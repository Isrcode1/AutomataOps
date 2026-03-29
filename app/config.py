import os
from dotenv import load_dotenv

load_dotenv()

TASKS_FOLDER = os.getenv("TASKS_FOLDER", "tasks/pending")
COMPLETED_FOLDER = os.getenv("COMPLETED_FOLDER", "tasks/completed")
FAILED_FOLDER = os.getenv("FAILED_FOLDER", "tasks/failed")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOGS_FOLDER = os.getenv("LOGS_FOLDER", "logs")
LOG_FILE = os.path.join(LOGS_FOLDER, "engine.log")
