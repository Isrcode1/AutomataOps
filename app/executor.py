import os
import logging
import shutil
from dotenv import load_dotenv

load_dotenv()

COMPLETED_FOLDER = os.getenv("COMPLETED_FOLDER")
FAILED_FOLDER = os.getenv("FAILED_FOLDER")


def execute_task(task_path):
    try:
        with open(task_path, 'r') as file:
            content = file.read()

        logging.info(f"Executing task: {task_path}")
        logging.info(f"Task content: {content.strip()}")

        filename = os.path.basename(task_path)
        new_path = os.path.join(COMPLETED_FOLDER, filename)

        shutil.move(task_path, new_path)
        logging.info(f"Task moved to completed: {new_path}")

    except Exception as e:
        logging.error(f"Error executing {task_path}: {str(e)}")

        filename = os.path.basename(task_path)
        new_path = os.path.join(FAILED_FOLDER, filename)

        shutil.move(task_path, new_path)
        logging.info(f"Task moved to failed: {new_path}")
