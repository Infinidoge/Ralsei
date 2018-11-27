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

    config["RalseiAlias"] = {"d4": "!roll 1d4",
                             "d6": "!roll 1d6",
                             "d8": "!roll 1d8",
                             "d10": "!roll 1d10",
                             "d12": "!roll 1d12",
                             "d20": "!roll 1d20",
                             "d100": "!roll 1d100",
                             "d%": "!roll 1d100",}
    with open(alias_file, 'w') as configfile:
        config.write(configfile)


def read_alias(alias_file):
    config = configparser.ConfigParser()
    config.read(alias_file)
    try:
        config["RalseiAlias"]
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
