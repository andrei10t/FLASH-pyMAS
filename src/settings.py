import os
import os.path
import yaml
import yamlordereddictloader

from os.path import expanduser


class Struct:
    def __init__(self, **entries):
        self.__dict__.update(entries)

    def __getitem__(self, val):
        print(val)


class Settings(object):
    local_config_path = None

    def __init__(self):
        self.local_config_path = expanduser("~/.config/flash/flash.yaml")
        self.load_configfile()

    def load_configfile(self):
        config_data = None
        if os.path.isfile(self.config_path):
            config_data = yaml.load(
                open(self.config_path), Loader=yamlordereddictloader.Loader
            )
        else:
            print("flash.yaml not found in ~/.config/flash/")
            raise SystemExit(12)

        config_struct = Struct(**config_data)
        self.account = Struct(**config_struct.account)
