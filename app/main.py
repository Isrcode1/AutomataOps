import os
import logging
from dotenv import load_dotenv

from app.logger import setup_logger
from app.executor import execute_task

load_dotenv()

TASKS_FOLDER = os.getenv("TASKS_FOLDER")


def main():
    setup_logger()
    logging.info("AutomataOps engine started.")

    if not os.path.exists(TASKS_FOLDER):
        logging.error(f"Tasks folder '{TASKS_FOLDER}' does not exist.")
        return

    task_files = os.listdir(TASKS_FOLDER)

    if not task_files:
        logging.warning("No tasks found in the tasks folder.")
        return

    for task_file in task_files:
        task_path = os.path.join(TASKS_FOLDER, task_file)

        if os.path.isfile(task_path):
            execute_task(task_path)

    logging.info("AutomataOps engine finished processing tasks.")


if __name__ == "__main__":
    main()
