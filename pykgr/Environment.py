from multiprocessing import Process
from pykgr.util.Descriptions import get_class_from_file
from pykgr.util.Crypto import hash_string
from pykgr.util.Builder import build_from_class
from pykgr.Package import Package

class Environment(object):
    def build(self, script_file_name):
        runner = Process(target=build_from_class, args=(script_file_name, self))
        runner.start()

        runner.join()