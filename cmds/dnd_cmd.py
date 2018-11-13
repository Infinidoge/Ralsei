# ----------------------------------
# Ralsei/cmds/dnd_cmd
# Created by Infinidoge
# ----------------------------------
# Archetype command and general file to contain D&D related commands, such as rolling for a character stat block, etc.
# ----------------------------------

import random
from utils.permissions import Perms
perms = Perms()


async def stats(client, message):
    stat_total = 0
    while stat_total < 70:
        stat_block = []
        # Generate the main stats
        for i in range(6):
            rand = random.randint(1, 20)
            # Re-roll below 6
            while rand < 6:
                rand = random.randint(1, 20)
            stat_block.append(rand)
        stat_block.sort()
        # Re-roll the lowest
        rand = random.randint(1, 20)
        if rand > stat_block[0]:
            stat_block[0] = rand
            stat_block.sort()

        stat_total = sum(stat_block)

    # Convert everything above 18 into 18, with the original number in parenthesis
    for i in range(len(stat_block)):
        if stat_block[i] > 18:
            stat_block[i] = "18 (%s)" % str(stat_block[i])

    await client.send_message(message.channel, "[<@%s>]\n{%s}" % (message.author.id,
                                                                  str(" - ".join([str(i)
                                                                                  for i in stat_block]))))


subcmd = {"stats": stats}


async def dnd_cmd(client, message):
    cmd = message.content[5:]
    await subcmd[cmd.split(' ')[0]](client, message)
