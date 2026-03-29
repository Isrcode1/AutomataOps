import os
import logging
import shutil

from app.config import COMPLETED_FOLDER, FAILED_FOLDER


def execute_task(task_path):
    filename = os.path.basename(task_path)

    try:
        with open(task_path, "r") as file:
            content = file.read()

        logging.info(f"Executing task: {task_path}")
        logging.info(f"Task content: {content.strip()}")

        os.makedirs(COMPLETED_FOLDER, exist_ok=True)
        new_path = os.path.join(COMPLETED_FOLDER, filename)
        shutil.move(task_path, new_path)

        logging.info(f"Task moved to completed: {new_path}")

    except Exception as e:
        logging.error(f"Error executing {task_path}: {str(e)}")

        if os.path.exists(task_path):
            os.makedirs(FAILED_FOLDER, exist_ok=True)
            new_path = os.path.join(FAILED_FOLDER, filename)
            shutil.move(task_path, new_path)
            logging.info(f"Task moved to failed: {new_path}")
