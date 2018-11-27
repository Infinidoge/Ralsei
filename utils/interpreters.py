from enum import Enum, auto
import re


class RetCode(Enum):
    TOO_LONG = 0
    INVALID = auto()
    NO_PROG = auto()
    SUCCESS = auto()


def hq_interp(program):
    # check
    if len(program) > 30:
        return RetCode.TOO_LONG
    elif len(program) <= 0:
        return RetCode.NO_PROG
    elif program.count('9') > 1:
        return RetCode.INVALID

    output = ""  # the program output
    var = 0  # the useless var from the language

    if program.lower() == "help":
        output

    for i in program.lower():
        if i == "h":
            output += "Hello, World!\n"
        elif i == "q":
            output += program
        elif i == "9":
            for x in range(10, 1, -1):
                output += f"{x} bottles of beer on the wall,\n{x} bottles of beer.\nTake one down, pass it around,"

                if i == 2:
                    output += f"1 bottle of beer on the wall.\n"
                elif i == 1:
                    output += f"No more bottles of beer on the wall."
                else:
                    output += f"{x-1} bottles of beer on the wall."
        elif i == "+":
            var += 1
    return output
