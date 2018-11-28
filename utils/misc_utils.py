# ----------------------------------
# Ralsei/utils/misc_utils
# Created by Infinidoge
# ----------------------------------
# File to contain the miscellaneous utilities that might be needed for the bot, such as finding all files in a folder
# ----------------------------------

from os import listdir
from os.path import isfile, join


def find_files(path):
    return [f for f in listdir(path) if isfile(join(path, f))]


def capital(self: str):
    r = ""
    for i in self:
        r += i.capitalize()
    return r

