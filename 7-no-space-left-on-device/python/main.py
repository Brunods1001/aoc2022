from functools import reduce
from pathlib import Path
import re
from typing import Any, Generator, Tuple

from enum import Enum, auto

TESTDATA = Path(__file__).parent.parent / "test_data.txt"
DATA = Path(__file__).parent.parent / "data.txt"

SIZE = 100000
DIRSIZE: int = 0


class Msg(Enum):
    AddToDir = auto()
    AddToTotal = auto()
    CheckDirSize = auto()
    Continue = auto()


def read_data(file) -> Generator[str, None, None]:
    with open(file, "r") as f:
        while line := f.readline():
            yield line


def process_line(line: str) -> Tuple[Msg, Any]:
    """
    Reads line and decides which message to send
    """
    breakpoint()
    num, _ = line.split()
    if num.isnumeric():
        filesize = int(num)
        return (Msg.AddToDir, filesize)
    else:
        return (Msg.Continue, 0)


def update(msg: Msg, value) -> int:
    """
    Returns 0 or file size
    """
    global DIRSIZE
    breakpoint()
    match msg:
        case msg.Continue:
            return 0
        case msg.AddToDir:
            DIRSIZE += value
        case msg.CheckDirSize:
            if DIRSIZE > SIZE:
                update(msg.AddToTotal, DIRSIZE)
        case msg.AddToTotal:
            newsize = DIRSIZE
            DIRSIZE = 0
            return newsize
    raise Exception("No cases match")


def part1(file):
    """
    Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?
    """
    # tot = 0
    # look for cd <dir>\nls
    # then read each line until not a number
    # get the sum of the number
    # if the sum is greater than 100000, add it to tot
    lines = read_data(file)
    return reduce(lambda tot, line: tot + update(*process_line(line)), lines, 0)


def part2(file):
    ...


def main():
    res = part1(TESTDATA)


if __name__ == "__main__":
    main()
