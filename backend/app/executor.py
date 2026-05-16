import os
import logging
import shutil

from app.config import COMPLETED_FOLDER, FAILED_FOLDER


def move_task(task_path, destination_folder):
    os.makedirs(destination_folder, exist_ok=True)
    filename = os.path.basename(task_path)
    new_path = os.path.join(destination_folder, filename)
    shutil.move(task_path, new_path)
    return new_path


def execute_task(task_path):
    try:
        if not os.path.exists(task_path):
            raise FileNotFoundError(f"{task_path} not found")

        with open(task_path, "r") as file:
            content = file.read()

        if not content.strip():
            raise ValueError("Task file is empty")

        logging.info(f"Executing task: {task_path}")
        logging.info(f"Task content: {content.strip()}")

        new_path = move_task(task_path, COMPLETED_FOLDER)
        logging.info(f"Task moved to completed: {new_path}")

    except FileNotFoundError as e:
        logging.error(f"[FILE ERROR] {str(e)}")

    except ValueError as e:
        logging.error(f"[VALIDATION ERROR] {str(e)}")
        if os.path.exists(task_path):
            new_path = move_task(task_path, FAILED_FOLDER)
            logging.info(f"Task moved to failed: {new_path}")

    except PermissionError as e:
        logging.error(f"[PERMISSION ERROR] {str(e)}")
        if os.path.exists(task_path):
            new_path = move_task(task_path, FAILED_FOLDER)
            logging.info(f"Task moved to failed: {new_path}")

    except Exception as e:
        logging.error(f"[UNKNOWN ERROR] {str(e)}")
        if os.path.exists(task_path):
            new_path = move_task(task_path, FAILED_FOLDER)
            logging.info(f"Task moved to failed: {new_path}")
