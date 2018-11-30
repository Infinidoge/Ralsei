# ----------------------------------
# Ralsei/cmds/test_cmd
# Created by Infinidoge
# ----------------------------------
# Used to test permissions with decorators
# ----------------------------------


from utils.permissions import Perms
from utils.config import Client
perms, config = Perms(), Client()


@perms.check_dev
async def test_dev(client, message):
    await client.send_message(message.channel, "You seem to have the developer permission, good job.")


@perms.check_owner
async def test_owner(client, message):
    await client.send_message(message.channel, "You seem to have the owner permission, good job.")


async def test_perms(client, message):
    await client.send_message(message.channel, perms.permissions[message.author.id])


@perms.check_perms("admin")
async def test_permission(client, message):
    await client.send_message(message.channel, "HUZZAH!")


subcmd = {"dev":   test_dev,
          "owner": test_owner,
          "perms": test_perms,
          "permission": test_permission}


async def test_cmd(client, message):
    cmd = message.content[5+len(config.prefix):].split(" ")

    try:
        await subcmd[cmd[0]](client, message)
    except KeyError:
        await  client.send_message(message.channel, "Not a subcommand, whoops!")
