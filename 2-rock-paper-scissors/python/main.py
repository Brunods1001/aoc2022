from typing import Generator
from pathlib import Path
from functools import reduce

FILE = Path(__file__).parent.parent / "data.txt"
TESTFILE = Path(__file__).parent.parent / "testdata.txt"


def read_data(file) -> Generator[str, None, None]:
    with open(file, "r") as f:
        while line := f.readline():
            yield line

def part1(file):
    print("Part 1")
    result_points = {
            ("A", "X"):3,
            ("A", "Y"):6,
            ("A", "Z"):0,
            ("B", "X"):0,
            ("B", "Y"):3,
            ("B", "Z"):6,
            ("C", "X"):6,
            ("C", "Y"):0,
            ("C", "Z"):3,
            }
    choice_points = dict(
            X=1,
            Y=2,
            Z=3,
            )
    tot = 0
    for line in read_data(file):
        op, me = line.split()
        # points for matching
        p1 = choice_points[me]
        # points for game
        assert (op, me) in result_points.keys()
        p2: int = result_points[(op, me)]
        tot += p1 + p2 
    print("Total:", tot)

def part2(file):
    """
    X means you need to lose
    Y means you need to tie
    Z means you need to win
    """
    print("Part 2")
    result_points = {
            ("A", "A"):3,
            ("A", "B"):6,
            ("A", "C"):0,
            ("B", "A"):0,
            ("B", "B"):3,
            ("B", "C"):6,
            ("C", "A"):6,
            ("C", "B"):0,
            ("C", "C"):3,
            }
    rules = {
            ("A", "X"):"C",
            ("A", "Y"):"A",
            ("A", "Z"):"B",
            ("B", "X"):"A",
            ("B", "Y"):"B",
            ("B", "Z"):"C",
            ("C", "X"):"B",
            ("C", "Y"):"C",
            ("C", "Z"):"A",
            }
    choice_points = dict(
            A=1,
            B=2,
            C=3,
            )
    tot = 0
    for line in read_data(file):
        op, need = line.split()
        me = rules[(op, need)]
        p1 = choice_points[me]
        assert (op, me) in result_points.keys()
        p2: int = result_points[(op, me)]
        tot += p1 + p2
    print("Total:", tot)

def process(line):
    result_points = {
            ("A", "X"):3,
            ("A", "Y"):6,
            ("A", "Z"):0,
            ("B", "X"):0,
            ("B", "Y"):3,
            ("B", "Z"):6,
            ("C", "X"):6,
            ("C", "Y"):0,
            ("C", "Z"):3,
            }
    choice_points = dict(
            X=1,
            Y=2,
            Z=3,
            )
    op, me = line.split()
    # points for matching
    p1 = choice_points[me]
    # points for game
    assert (op, me) in result_points.keys()
    p2: int = result_points[(op, me)]
    return p1 + p2

def part1_reduce():
    print("Part 1 reduce")
    tot = reduce(process, read_data(file), 0)
    print(tot)
    print("Total:", tot)

def main():
    part1(TESTFILE)  # expect 15
    part1(FILE)
    part2(TESTFILE)  # expect 12
    part2(FILE)

if __name__ == "__main__":
    main()
