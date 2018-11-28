# ----------------------------------
# Ralsei/cmds/shutdown_cmd
# Created by Infinidoge
# ----------------------------------
# Provides the simple base command to shut down the bot safely, alleviates the need to kill the process
# ----------------------------------

from utils.permissions import Perms
perms = Perms()


@perms.check_owner
async def shutdown_cmd(client, message):
    await client.send_message(message.channel, "Goodbye!")
    await client.close()
