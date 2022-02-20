from os import environ
from re import findall as findall

configuration_dict = {
    "directory": "/opt/pykgr",
    "system_directory": "{directory}/system",
    "build_directory": "{directory}/builds"
}

class Configuration(object):
    def __init__(self):
        self.build_config()

    def build_config(self):
        for key in configuration_dict:
            ext_key = f"pykgr_{key}"
            envar = environ.get(ext_key)
            value = envar if envar else configuration_dict[key]
            
            replaceable_instances = findall("{(.*?)}", value)
            if len(replaceable_instances):
                for var in replaceable_instances:
                    value = value.replace("{" + var + "}", getattr(self, var))
            
            setattr(self, key, value)

def get_config():
    return Configuration()