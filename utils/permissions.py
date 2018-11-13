# ----------------------------------
# Ralsei/utils/permissions
# Created by Infinidoge
# ----------------------------------
# Utility for managing the permissions config file. Formatted almost the same as Ralsei/utils/config, except
# specialized to managing the permissions file
# ----------------------------------

import configparser

def gen_perms(perms_file):
    config = configparser.ConfigParser()

    config["RalseiPerms"] = {"owner": "blank"}
    with open(perms_file, 'w') as configfile:
        config.write(configfile)


def read_perms(perms_file):
    config = configparser.ConfigParser()
    config.read(perms_file)
    try:
        return config["RalseiPerms"]
    except:
        gen_perms(perms_file)
        read_perms(perms_file)


class Perms:
    def __init__(self, perms_file="RalseiPerms.ini"):
        perms = read_perms(perms_file)
        self.owner_id = perms["owner"]

    def check_owner(self, message):
        return True if (self.owner_id == message.author.id) else False
