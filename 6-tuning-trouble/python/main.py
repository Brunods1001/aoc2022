from functools import reduce
from pathlib import Path
import re
from typing import Generator, Set, Tuple

TESTDATA = Path(__file__).parent.parent / "test_data.txt"
TESTDATA2 = Path(__file__).parent.parent / "test_data_2.txt"
DATA = Path(__file__).parent.parent / "data.txt"

Stacks = dict[str, list[str]]

def read_data(file) -> Generator[Stacks | str, None, None]:
    with open(file, "r") as f:
        while line := f.readline():
            yield line
        
def process_line(line) -> int:
    assert len(line) >= 4, "Line not long enough to contain signal"
    chars = list(line)
    idx0 = 0
    idxf = 4
    while idxf <= len(line):
        buf: Set = set(chars[idx0:idxf])
        if len(buf) == 4:
            return idxf
        idx0 += 1
        idxf += 1
    raise Exception("No signal found")



def process_line_part2(line) -> int:
    n = 14
    assert len(line) >= n, "Line not long enough to contain signal"
    chars = list(line)
    idx0 = 0
    idxf = n
    while idxf <= len(line):
        buf: Set = set(chars[idx0:idxf])
        if len(buf) == n:
            return idxf
        idx0 += 1
        idxf += 1
    raise Exception("No signal found")


def part1(file) -> Generator[int, None, None]:
    """
    The start of a packet is indicated by a sequence of four characters that are all different.

    Identify the first position where the four most recently received characters were all different.

    How many characters need to be processed before the first start-of-packet marker is detected?
    """
    lines = read_data(file)
    for line in lines:
        yield process_line(line)

def part2(file) -> Generator[int, None, None]:
    """
    A start-of-message marker is just like a start-of-packet marker, except it consists of 14 distinct characters rather than 4.
    """
    lines = read_data(file)
    for line in lines:
        yield process_line_part2(line)

def main():
    res = list(part1(TESTDATA))
    assert res[0] == 5, f"res is {res}"
    assert res[1] == 6, f"res is {res}"
    assert res[2] == 10, f"res is {res}"
    assert res[3] == 11, f"res is {res}"
    print("Part 1 test:", res)
    res = part1(DATA)
    print("Part 1:", next(res))

    res = list(part2(TESTDATA2))
    assert res[0] == 19, f"res is {res}"
    assert res[1] == 23, f"res is {res}"
    assert res[2] == 23, f"res is {res}"
    assert res[3] == 29, f"res is {res}"
    assert res[4] == 26, f"res is {res}"
    print("Part 2 test:", res)
    res = part2(DATA)
    print("Part 2:", next(res))

if __name__ == "__main__":
    main()

