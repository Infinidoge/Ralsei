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

    config["RalseiPerms"] = {"owner": "blank",
                             "developers": "blank",
                             "denied_statement": "You don't have permission, sorry!"}
    config["RalseiGroups"] = {}
    with open(perms_file, 'w') as configfile:
        config.write(configfile)


def read_perms(perms_file):
    config = configparser.ConfigParser()
    config.read(perms_file)
    try:
        config["RalseiPerms"]["owner"]
        return config
    except:
        gen_perms(perms_file)
        read_perms(perms_file)


class Perms:
    def __init__(self, perms_file="RalseiPerms.ini"):
        perms = read_perms(perms_file)

        # Developer and owner IDs
        self.owner_id = perms["RalseiPerms"]["owner"]
        self.developer_ids = perms["RalseiPerms"]["developers"].split(";")

        # Permissions messages
        self.denied = perms["RalseiPerms"]["denied_statement"]

        # Groups setup
        self.permissions = {}
        for i in perms["RalseiGroups"].keys():
            self.permissions[i] = perms["RalseiGroups"][i].split(";")

    def check_owner(self, func):
        owner_id = self.owner_id
        denied = self.denied

        async def inner(client, message):
            if owner_id != message.author.id:
                await client.send_message(message.channel, denied)
                return
            else:
                await func(client, message)
                return

        return inner

    def check_dev(self, func):
        developer_ids = self.developer_ids
        denied = self.denied

        async def inner(client, message):
            if message.author.id not in developer_ids:
                await client.send_message(message.channel, denied)
                return
            else:
                await func(client, message)
                return

        return inner

    def check_admin(self, func):
        owner_id = self.owner_id
        developer_ids = self.developer_ids
        denied = self.denied
        perms = self.permissions

        async def inner(client, message):
            if message.author.id not in developer_ids \
                    and message.author.id != owner_id \
                    and "admin" not in perms[message.author.id]:

                await client.send_message(message.channel, denied)
                return
            else:
                await func(client, message)
                return

        return inner

    def check_perms(self, permission):
        owner_id = self.owner_id
        developer_ids = self.developer_ids
        denied = self.denied
        perms = self.permissions

        def inner(func):
            async def wrapper(client, message):
                author = message.author.id
                try:
                    if permission in perms[author] or author in developer_ids or author is owner_id:
                        await func(client, message)
                    else:
                        await  client.send_message(message.channel, denied)
                except KeyError:
                    await  client.send_message(message.channel, denied)

            return wrapper

        return inner
