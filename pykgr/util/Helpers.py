from os.path import exists
from os import mkdir
import subprocess


def create_filesystem():
    directories = ["bin", "etc"]
    if not exists("/opt/pykgr"):
        print("Please create /opt/pykgr and set it's owner to your user")
        exit(-1)

    if not exists("/opt/pykgr/system"):
        create_recursive_directory("/opt/pykgr/system")

    for d in directories:
        subdir = f"/opt/pykgr/system/{d}"
        if not exists(subdir):
            create_recursive_directory(subdir)


def create_recursive_directory(dir_path):
    whole_path = "";
    for subdir in dir_path.split("/"):
        if subdir:
            whole_path += f"/{subdir}"
            
            if not exists(whole_path):
                mkdir(whole_path)


def run_cmd(*args):
    subprocess.run(args)
