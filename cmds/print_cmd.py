# ----------------------------------
# Ralsei/cmds/print_cmd
# Created by Infinidoge
# ----------------------------------
# Echos the message the user send as the bot, subtracting the command itself. ([prefix]print)
# ----------------------------------

from utils.permissions import Perms
from utils.config import Client
perms, config = Perms(), Client()


@perms.check_perms("admin")
async def print_cmd(client, message):
    await client.send_message(message.channel, message.content[6+len(config.prefix):])
