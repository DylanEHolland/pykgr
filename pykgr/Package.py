from pykgr.util.Crypto import hash_string

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
        directory = f"/tmp/pykgr/build/{cls.__name__}-{hash_string(cls.source_tarball)}"

        if(directory == "/"): raise PermissionError("Trying to delete ROOT")
        return directory

    def compile(self):
        # Should be overwritten
        pass

    def post_compile(self):
        # Should be overwritten
        pass

    def prepare(self):
        pass

    def pre_compile(self):
        # Should be overwritten
        pass
