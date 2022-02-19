from pykgr.util.Descriptions import get_class_from_file
from pykgr.util.Source import extract_source_from_url
from pykgr.util.Helpers import create_recursive_directory, run_cmd
from os.path import exists

from os import chdir, mkdir
from os.path import exists


def build_from_class(script_file_name, env):
    package_class = get_class_from_file(script_file_name)
    package = package_class(env)

    if exists(package.build_directory()):
        run_cmd("rm", "-rfv", package.build_directory())

    create_recursive_directory(package.build_directory())
    chdir(package.build_directory())
    
    extract_source_from_url(package.source_tarball)
    package.build()