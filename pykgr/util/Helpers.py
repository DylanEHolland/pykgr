from os.path import exists
from os import mkdir
import subprocess


def create_recursive_directory(dir_path):
    whole_path = "";
    for subdir in dir_path.split("/"):
        if subdir:
            whole_path += f"/{subdir}"
            
            if not exists(whole_path):
                mkdir(whole_path)


def run_cmd(*args):
    subprocess.run(args)
