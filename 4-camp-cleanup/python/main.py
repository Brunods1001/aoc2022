from functools import reduce
from pathlib import Path
from typing import Generator

TESTDATA = Path(__file__).parent.parent / "test_data.txt"
DATA = Path(__file__).parent.parent / "data.txt"


def read_data(file) -> Generator[str, None, None]:
    with open(file, "r") as f:
        while line := f.readline():
            yield line

def process_line(line: str) -> int:
    r1, r2 = line.split(",")
    r1_1, r1_2 = [int(i) for i in r1.split("-")]
    r2_1, r2_2 = [int(i) for i in r2.split("-")]
    condition1 = r1_1 <= r2_1 and r1_2 >= r2_2
    condition2 = r1_1 >= r2_1 and r1_2 <= r2_2
    res = condition1 or condition2
    return int(res)

def process_line_part2(line: str) -> int:
    r1, r2 = line.split(",")
    r1_1, r1_2 = [int(i) for i in r1.split("-")]
    r2_1, r2_2 = [int(i) for i in r2.split("-")]
    condition1 = r1_1 <= r2_1 and r1_2 >= r2_2
    condition2 = r1_1 >= r2_1 and r1_2 <= r2_2
    condition3 = r1_1 >= r2_1 and r1_1 <= r2_2
    condition4 = r1_2 >= r2_1 and r1_2 <= r2_2
    res = condition1 or condition2 or condition3 or condition4
    return int(res)
                
def part1(file):
    """
    In how many assignment pairs does one range fully contain the other?
    """
    lines = read_data(file)
    return reduce(lambda tot, line: process_line(line) + tot, lines, 0)
                
def part2(file):
    """
    In how many assignment pairs do the ranges overlap?
    """
    lines = read_data(file)
    return reduce(lambda tot, line: process_line_part2(line) + tot, lines, 0)

def main():
    res = part1(TESTDATA)
    assert res == 2, f"res is {res}"
    print("Part 1 test:", res)
    res = part1(DATA)
    print("Part 1:", res)

    res = part2(TESTDATA)
    assert res == 4, f"res is {res}"
    print("Part 2 test:", res)
    res = part2(DATA)
    print("Part 2:", res)

if __name__ == "__main__":
    main()
