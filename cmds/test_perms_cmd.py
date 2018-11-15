# ----------------------------------
# Ralsei/cmds/test_perms_cmd
# Created by Infinidoge
# ----------------------------------
# Used to test permissions with decorators
# ----------------------------------


from utils.permissions import Perms
perms = Perms()


@perms.check_dev
async def test_perms_cmd(client, message):
    await client.send_message(message.channel, "You seem to have permission, good job.")