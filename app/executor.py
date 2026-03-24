import os
import logging


def execute_task(task_path):
    try:
        with open(task_path, 'r') as file:
            content = file.read()

        logging.info(f"Executing task: {task_path}")
        logging.info(f"Task content: {content.strip()}")

    except Exception as e:
        logging.error(f"Error executing {task_path}: {str(e)}")
