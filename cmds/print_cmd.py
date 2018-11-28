# ----------------------------------
# Ralsei/cmds/print_cmd
# Created by Infinidoge
# ----------------------------------
# Echos the message the user send as the bot, subtracting the command itself. ([prefix]print)
# ----------------------------------

from utils.permissions import Perms
perms = Perms()


@perms.check_owner
async def print_cmd(client, message):
    await client.send_message(message.channel, message.content[7:])
