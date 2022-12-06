from functools import reduce
from pathlib import Path
import re
from typing import Generator, Tuple

TESTDATA = Path(__file__).parent.parent / "test_data.txt"
DATA = Path(__file__).parent.parent / "data.txt"

Stacks = dict[str, list[str]]

def read_data(file) -> Generator[Stacks | str, None, None]:
    with open(file, "r") as f:
        stacks = read_stacks(f)
        yield stacks
        while line := f.readline():
            yield line
        

def read_stacks(f) -> Stacks:
    """
    Returns stacks in data as a stackname:stacks pair, where stacks is in
    ascending order.
    """
    # read until newline
    stacks: Stacks = {}
    rows = []
    keys = None
    n = 4  # delimit by n chars
    while (line := f.readline()) != "\n":
        # delimit by spaces
        values: list[str] = [line[i:i+n].strip() for i in range(0, len(line), n)]
        rows.append(values)
    keys = rows.pop()
    assert keys is not None, "Keys not found"
    for row in rows:
        for k, val in zip(keys, row):
            try:
                stacks[k].append(val)
            except KeyError:
                stacks[k] = [val]
    stacks = {k: [i for i in v if i][-1::-1] for k, v in stacks.items()}
    return stacks

def process_line(stacks, line) -> Stacks:
    res = re.split("move|from|to", line)
    num_move, key_from, key_to = [i.strip() for i in res if i.strip()]
    num_move = int(num_move)
    vals = [stacks[key_from].pop() for _ in range(num_move)]
    stacks[key_to] += vals
    return stacks

def process_stacks(stacks) -> str:
    res = []
    for _, v in stacks.items():
        res.append(v.pop().replace("[", "").replace("]", ""))
    return "".join(res)

def part1(file):
    """
    After the rearrangement procedure completes, what crate ends up on top of 
    each stack?
    """
    lines = read_data(file)
    stacks = next(lines)
    # stacks is mutable and not concurrent because its state
    # depends on each line

    # dict is mutable
    stacks_final = reduce(lambda tot, line: process_line(tot, line), lines, stacks)
    return process_stacks(stacks_final)

def part2(file):
    ...

def main():
    lines = read_data(TESTDATA)
    stacks = next(lines)
    res = part1(TESTDATA)
    assert res == "CMZ", f"res is {res}"
    print("Part 1 test:", res)
    res = part1(DATA)
    print("Part 1:", res)

    # res = part2(TESTDATA)
    # assert res == 4, f"res is {res}"
    # print("Part 2 test:", res)
    # res = part2(DATA)
    # print("Part 2:", res)

if __name__ == "__main__":
    main()
