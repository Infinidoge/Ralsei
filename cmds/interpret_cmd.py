# ----------------------------------
# Ralsei/cmds/interpret_cmd
# Created by Infinidoge
# ----------------------------------
# Takes a segment of code within a code block and interprets it based on the coding language you input.
# Currently Supports:
# HQ9+
# ----------------------------------

from utils.interpreters import hq_interp
import discord


async def interpret_cmd(client, message):
    cmd = message.content[11:]
    cmd = cmd.split(" ")
    if cmd[0] == "HQ9+":
        await client.send_message(message.channel,
                                  embed=discord.Embed(
                                      title="HQ9+ Interpret",
                                      description=hq_interp(cmd[1])
                                  ))
    else:
        await client.send_message(message.content,
                                  "That doesn't seem to be a coding language.")
