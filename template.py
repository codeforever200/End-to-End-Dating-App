import os
from pathlib import Path
import logging

# to get information level log and error messages
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "datingapp"

# creating files within the folder
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    "bios.ipynb"


]

for filepath in list_of_files:
    filepath = Path(filepath)      # in order to get path in windows format
    filedir, filename = os.path.split(filepath)

# if folder not empty create file directory
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")