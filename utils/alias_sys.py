# ----------------------------------
# Ralsei/utils/alias_sys
# Created by Infinidoge
# ----------------------------------
# Utility base for creating aliases for commands
# ----------------------------------

from cmds.roll_cmd import roll_cmd
from utils.permissions import Perms
perms = Perms()


class Alias:
    async def d20(self, client):
        print("d20_run")
        await roll_cmd(client, "!roll 1d20")

    def __init__(self):
        self.alias = {"d20": self.d20}

    def __call__(self, cmd):
        try:
            self.alias[cmd]
        except KeyError:
            raise KeyError
