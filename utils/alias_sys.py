# ----------------------------------
# Ralsei/utils/alias_sys
# Created by Infinidoge
# ----------------------------------
# Utility base for creating aliases for commands
# ----------------------------------

from cmds.roll_cmd import roll_cmd
from utils.permissions import Perms
import asyncio
perms = Perms()


class Alias:
    async def d20(self, client, message):
        print("d20_run")
        message.content = "!roll 1d20"
        await roll_cmd(client, message)

    def __init__(self):
        print("alias_init")
        self.alias = {"d20": self.d20}

    async def __call__(self, cmd, client, message):
        print("alias_called")
        try:
            await self.alias[cmd](client, message)
            print(cmd)
        except KeyError:
            print("key error")
            raise KeyError
