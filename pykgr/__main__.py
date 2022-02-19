from argparse import ArgumentParser
# from pykgr.Subroutines import get_class_from_file
from pykgr.Environment import Environment

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("-b", "--build", help="Build a package file")

    return parser.parse_args()

args = parse_args()
if args.build:
    env = Environment()
    env.build(args.build)
