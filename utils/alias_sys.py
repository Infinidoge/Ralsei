# ----------------------------------
# Ralsei/utils/alias_sys
# Created by Infinidoge
# ----------------------------------
# Utility base for creating aliases for commands
# ----------------------------------

from utils.permissions import Perms
import configparser
perms = Perms()


def gen_alias(alias_file):
    config = configparser.ConfigParser()

    config["RalseiAlias"] = {"token": "blank",
                             "prefix": "!",
                             "location": "blank"}
    with open(alias_file, 'w') as configfile:
        config.write(configfile)


def read_alias(alias_file):
    config = configparser.ConfigParser()
    config.read(alias_file)
    try:
        return config
    except:
        gen_alias(alias_file)
        read_alias(alias_file)


def update_config():
    pass


class Alias:

    def __init__(self, alias_file="RalseiAlias.ini"):
        aliasconfig = read_alias(alias_file)
        self.alias = {}
        for i in aliasconfig["RalseiAlias"].keys():
            self.alias[i] = aliasconfig["RalseiAlias"][i]

    def __call__(self, cmd, message):
        try:
            message.content = self.alias[cmd]
            return message
        except KeyError:
            raise KeyError
