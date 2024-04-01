import os
from pathlib import Path
import logging    #Logging in Python allows developers to record messages at various levels of severity and route them to different outputs. The logging module in Python provides a flexible framework for implementing logging in applications.

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "cnnClassifier"

list_of_files = [
    ".github/workflows/.gitkeep",   #.gitkeep files are typically used to ensure that empty directories are kept in Git repositories.
    f"src/{project_name}/__init__.py",  #The __init__.py file is used to mark the directory as a Python package.
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",   # used for version control and tracking data and models with Data Version Control (DVC).
    "params.yaml",  #YAML, which stands for "YAML Ain't Markup Language," is a human-readable data serialization format commonly used for configuration files, data exchange, and representing hierarchical data structures. 
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")   

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")    