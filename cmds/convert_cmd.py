# ----------------------------------
# Ralsei/cmds/convert_cmd
# Created by Infinidoge
# ----------------------------------
# Command to convert between currencies. May be updated to allow conversion of other mediums, such as units or timezones
# ----------------------------------

from utils.converter import convert
from utils.permissions import Perms
perms = Perms()


subcmd = {}


async def convert_cmd(client, message):
    cmd = message.content[9:]
    print(cmd)
    currency, amount = cmd.split(" ")
    currency, amount = currency.split("-"), int(amount)
    await client.send_message(message.channel, "[<@%s>]\n**Currency Conversion:** %s *to* %s\n`%s`**%** is `%s`**%s**"
                              % (str(message.author.id), currency[0], currency[1],
                                 str(amount), currency[0], convert(amount, currency[0], currency[1]), currency[1]))


    # cmd = message.content[5:]
    # await subcmd[cmd.split(' ')[0]](client, message)
