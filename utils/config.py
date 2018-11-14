# ----------------------------------
# Ralsei/utils/config.py
# Created by Infinidoge
# ----------------------------------
# Utility for managing the Ralsei config file, can generate and read the config and has room to add updating the config
# as well
# ----------------------------------

import configparser


def gen_config(config_file):
    config = configparser.ConfigParser()

    config["Ralsei"] = {"token": "blank",
                        "prefix": "!",
                        "location": "blank",
                        "alias": True}
    with open(config_file, 'w') as configfile:
        config.write(configfile)


def read_config(config_file):
    config = configparser.ConfigParser()
    config.read(config_file)
    try:
        return config
    except:
        gen_config(config_file)
        read_config(config_file)


def update_config():
    pass


class Client:
    def __init__(self, config_file="Ralsei.ini"):
        config = read_config(config_file)
        self.token = config["Ralsei"]["token"]
        self.prefix = config["Ralsei"]["prefix"]
        self.location = config["Ralsei"]["location"]
        self.alias = config["Ralsei"].getboolean("alias")
