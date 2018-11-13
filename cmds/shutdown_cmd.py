# ----------------------------------
# Ralsei/cmds/shutdown_cmd
# Created by Infinidoge
# ----------------------------------
# Provides the simple base command to shut down the bot safely, alleviates the need to kill the process
# ----------------------------------

from utils.permissions import Perms
perms = Perms()


async def shutdown_cmd(client, message):
    if perms.check_owner(message):
        await client.send_message(message.channel, "Goodbye!")
        await client.close()
    else:
        await client.send_message(message.channel, "You do not have permission to run this command.")