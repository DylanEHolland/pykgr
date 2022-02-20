from pykgr.Environment import Environment
from pykgr.util.Helpers import create_filesystem

from argparse import ArgumentParser
from os.path import exists

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("-b", "--build", help="Build a package file")
    parser.add_argument("--init", action="store_true", help="Initialize the pykgr filesystem")

    return parser.parse_args()

args = parse_args()

if not exists("/opt/pykgr"):
    print("Please create /opt/pykgr and give yourself permissions to read/write to it")
    exit(-1)

if not args.init:
    if not exists("/opt/pykgr/system"):
        print("Please run --init")
        exit(-1)
else:
    create_filesystem()


if args.build:
    env = Environment()
    env.build(args.build)
