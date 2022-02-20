from os import environ
from re import findall as findall

configuration_dict = {
    "pykgr_directory": "/opt/pykgr",
    "pykgr_system_directory": "{pykgr_directory}/system"
}

class Configuration(object):
    def __init__(self):
        self.build_config()

    def build_config(self):
        for key in configuration_dict:
            envar = environ.get(key)
            value = envar if envar else configuration_dict[key]
            
            replaceable_instances = findall("{(.*?)}", value)
            if len(replaceable_instances):
                for var in replaceable_instances:
                    value = value.replace("{" + var + "}", getattr(self, var))
            
            setattr(self, key, value)