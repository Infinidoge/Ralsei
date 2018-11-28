# ----------------------------------
# Ralsei/cmds/convert_cmd
# Created by Infinidoge
# ----------------------------------
# Command to convert between currencies. May be updated to allow conversion of other mediums, such as units or timezones
# ----------------------------------

from utils.permissions import Perms
from utils.misc_utils import capital
from currency_converter import CurrencyConverter
c, perms = CurrencyConverter(), Perms()

subcmd = {}


async def convert_cmd(client, message):
    cmd = message.content[9:]
    currency, amount = cmd.split(" ")
    currency, amount = currency.split("-"), int(amount)
    currency[0], currency[1] = capital(currency[0]), capital(currency[1])
    await client.send_message(message.channel, "[<@%s>]\n**Currency Conversion:** %s *to* %s\n`%s`**%s** is `%s`**%s**"
                              % (str(message.author.id), currency[0], currency[1], str(amount), currency[0],
                                 round(c.convert(int(amount), currency[0], currency[1]), 2), currency[1]))

    # cmd = message.content[5:]
    # await subcmd[cmd.split(' ')[0]](client, message)
