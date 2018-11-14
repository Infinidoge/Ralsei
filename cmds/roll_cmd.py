# ----------------------------------
# Ralsei/cmds/roll_cmd
# Created by Infinidoge
# ----------------------------------
# Rolls a dice based on input from the user, in the format MdN [+ | - X]
# (X is the optional modifier for the entire dice roll)
# ----------------------------------

import random
import discord


async def roll_cmd(client, message):
    cmd = message.content[6:]
    print("roll_run")

    if "+" in cmd:
        pre = cmd.split("+")
        dice, mod = pre
        dice = dice.lower().split("d")
        if int(dice[0]) > 500 or int(dice[1]) > 1000:
            await client.send_message(message.channel,
                                      "Those numbers are a little too large for my handful of dice, sorry!")
            return
        rolls = []
        try:
            for i in range(int(dice[0])):
                roll = random.randint(1, int(dice[1]))
                rolls.append(roll)
            await client.send_message(message.channel, "[<@%s>]\n:game_die: Rolling: %sd%s:\n%s\nsum:%s" %
                                      (message.author.id,
                                       str(dice[0]),
                                       str(dice[1]),
                                       str("+".join(
                                           [str(i)
                                            for i in rolls]) +
                                           "**+%s**" % mod),
                                       str(sum(rolls) + int(mod))))
        except discord.errors.HTTPException:
            await client.send_message(message.channel,
                                      "Those numbers are a little too large for my handful of dice, sorry!")

    elif "-" in cmd:
        pre = cmd.split("-")
        dice, mod = pre
        dice = dice.lower().split("d")
        if int(dice[0]) > 500 or int(dice[1]) > 1000:
            await client.send_message(message.channel,
                                      "Those numbers are a little too large for my handful of dice, sorry!")
            return
        try:
            rolls = []
            for i in range(int(dice[0])):
                roll = random.randint(1, int(dice[1]))
                rolls.append(roll)
            await client.send_message(message.channel, "[<@%s>]\n:game_die: Rolling: %sd%s:\n%s\nsum:%s" %
                                      (message.author.id,
                                       str(dice[0]),
                                       str(dice[1]),
                                       str("+".join(
                                           [str(i)
                                            for i in rolls]) +
                                           "**-%s**" % mod),
                                       str(sum(rolls) - int(mod))))
        except discord.errors.HTTPException:
            await client.send_message(message.channel,
                                      "Those numbers are a little too large for my handful of dice, sorry!")

    else:
        cmd = cmd.lower().split("d")
        if int(cmd[0]) > 500 or int(cmd[1]) > 1000:
            await client.send_message(message.channel,
                                      "Those numbers are a little too large for my handful of dice, sorry!")
            return
        try:
            rolls = []
            for i in range(int(cmd[0])):
                roll = random.randint(1, int(cmd[1]))
                rolls.append(roll)
            await client.send_message(message.channel, "[<@%s>]\n:game_die: Rolling: %sd%s:\n%s\nsum:%s" %
                                      (message.author.id,
                                       str(cmd[0]),
                                       str(cmd[1]),
                                       str("+".join(
                                           [str(i)
                                            for i in rolls])),
                                       str(sum(rolls))))

        except discord.errors.HTTPException:
            await client.send_message(message.channel,
                                      "Those numbers are a little too large for my handful of dice, sorry!")
