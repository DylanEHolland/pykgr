from pykgr.util.Crypto import hash_string
from pykgr import config

class Package(object):
    env = None
    dependencies = {}

    def __init__(self, env):
        self.env = env

    def build(self):
        self.pre_compile()
        self.compile()
        self.post_compile()

    @classmethod
    def build_directory(cls):
        directory = f"/tmp/pykgr/build/{cls.__name__}-{cls.hash_name()}"

        if(directory == "/"): raise PermissionError("Trying to delete ROOT")
        return directory

    def compile(self):
        # Should be overwritten
        pass
    
    @classmethod
    def hash_name(cls):
        return hash_string(cls.source_tarball)

    @classmethod
    def installation_dir(cls):
        return f"{config.build_directory}/{cls.__name__}/{cls.hash_name()}"

    def post_compile(self):
        # Should be overwritten
        pass

    def prepare(self):
        pass

    def pre_compile(self):
        # Should be overwritten
        pass
