from os.path import exists, basename
from pykgr.Package import Package
from pykgr import config as Config

# This is the scope for package files, include stuff to be used there below
from pykgr.util.Helpers import run_cmd
from os import mkdir, chdir

def get_class_from_file(python_file):
    # Take a python file, run it and return
    # the class from within (not an instance of the class)
    #
    # The class name will always be the filename
    if not exists(python_file):
        return False

    with open(python_file, 'r') as fp:
        code = fp.read()
        fp.close()

    #Get classname
    class_name = basename(python_file).replace(".py", "")

    exec(code)
    return eval(f"{class_name}")