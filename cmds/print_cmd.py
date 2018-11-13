# ----------------------------------
# Ralsei/cmds/print_cmd
# Created by Infinidoge
# ----------------------------------
# Echos the message the user send as the bot, subtracting the command itself. ([prefix]print)
# ----------------------------------

from utils.permissions import Perms
perms = Perms()


async def print_cmd(client, message):
    if perms.check_owner(message):
        await client.send_message(message.channel, message.content[7:])
    else:
        await client.send_message(message.channel, "*Refuses to listen to <@" + message.author.id + ">*")