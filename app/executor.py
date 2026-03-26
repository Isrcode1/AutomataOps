import os
import logging
import shutil


def execute_task(task_path):
    try:
        with open(task_path, 'r') as file:
            content = file.read()

        logging.info(f"Executing task: {task_path}")
        logging.info(f"Task content: {content.strip()}")

        # Move to completed
        filename = os.path.basename(task_path)
        new_path = os.path.join("tasks/completed", filename)
        shutil.move(task_path, new_path)

        logging.info(f"Task moved to completed: {new_path}")

    except Exception as e:
        logging.error(f"Error executing {task_path}: {str(e)}")

        # Move to failed
        filename = os.path.basename(task_path)
        new_path = os.path.join("tasks/failed", filename)
        shutil.move(task_path, new_path)

        logging.info(f"Task moved to failed: {new_path}")
