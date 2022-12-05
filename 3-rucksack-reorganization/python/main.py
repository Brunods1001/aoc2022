from functools import reduce
from pathlib import Path
import string
from typing import Generator

TESTDATA = Path(__file__).parent.parent / "test_data.txt"
DATA = Path(__file__).parent.parent / "data.txt"


def read_data(file) -> Generator[str, None, None]:
    with open(file, "r") as f:
        while line := f.readline():
            yield line


def read_data_part_2(file, n: int = 3) -> Generator[str, None, None]:
    with open(file, "r") as f:
        lines = []
        while line := f.readline():
            lines.append(line)
            if len(lines) == n:
                yield "".join(lines)
                lines = []


def priority(letter: str) -> int:
    return 1 + string.ascii_letters.index(letter)


def process_line(line: str) -> int:
    letter = get_letter_from_line(line)
    return priority(letter)


def get_letter_from_line(line: str) -> str:
    line = line.strip()
    n_len = len(line)
    assert n_len != 0, "Line is empty"
    assert (
        n_len % 2 == 0
    ), f"Line does not have an even number of letters {n_len}: {line}"
    # find the item that appears in both compartments
    # get the set of letters in half the line
    s1 = set(line[: n_len // 2])
    # get the set of letters in the other half of the line
    s2 = set(line[n_len // 2 :])
    common = s1 & s2  # gets intersection between two sets
    assert len(common) == 1, f"One letter {common} not found in rucksack: {line}"
    return common.pop()


def reduce_lines_to_common_letters(lines: Generator[str, None, None]) -> set[str]:
    # convert line to list of chars and then to a set
    tot = set(list(next(lines)))
    return reduce(lambda tot, line: tot & set(list(line)), lines, tot)


def get_badge_from_lines(lines_txt: str) -> str:
    """
    Find the letter that appears in all lines
    """
    lines = (line for line in lines_txt.split("\n") if line)
    s = reduce_lines_to_common_letters(lines)
    assert len(s) == 1, breakpoint()  # "More than one letter found in group of elves"
    return s.pop()


def process_lines(lines: str) -> int:
    badge = get_badge_from_lines(lines)
    assert len(badge) == 1, "More than one badge found for the group"
    return priority(badge)


def part1(file) -> int:
    """
    Find the item type that appears in both compartments of each
    rucksack. What is the sum of the priorities of those item types?
    """
    return reduce(lambda tot, line: tot + process_line(line), read_data(file), 0)


def part2(file) -> int:
    """
    Find the item type that corresponds to the badges of each three-Elf group.
    What is the sum of the priorities of those item types?
    """
    # read in three lines at a time
    return reduce(
        lambda tot, lines: tot + process_lines(lines), read_data_part_2(file), 0
    )


def main():
    res = part1(TESTDATA)
    assert res == 157
    print("Part 1 test:", res)
    res = part1(DATA)
    print("Part 1:", res)

    # Part 2
    res = part2(TESTDATA)
    assert res == 70
    print("Part 2 test:", res)
    res = part2(DATA)
    print("Part 2:", res)


if __name__ == "__main__":
    main()
