import tempfile
from typing import Generator

def TEST_DATA() -> Generator[str, None, None]:
    with tempfile.TemporaryFile() as f:
        f.write(b"""1000
        2000
        3000

        4000

        5000
        6000

        7000
        8000
        9000

        10000""")
        f.seek(0)

        while line := f.readline():
            yield line.decode("utf8")

def split_data0(txt, sep):
    return (i for i in txt.split(sep) if i.isnumeric())

def main_test():
    idx = find_most_calories(TEST_DATA())
    print("Elf with most calories: #", idx, sep="\n")

def gen_data(num):
    from random import randint
    # a long long string
    sep = "\n"
    txt = sep.join(
        [f"{randint(1000, 10000)}" for _ in range(num)])
    return txt

def timeit(f):
    from time import time
    t1 = time()
    f()
    t2 = time()
    tt1 = t2 - t1
    print("Run:", tt1)

def split_test():
    from time import time
    t1 = time()
    main_test()
    t2 = time()
    tt1 = t2 - t1
    print("run1:", tt1)
    t1 = time()
    main_test()
    t2 = time()
    tt2 = t2 - t1
    print("run2:", tt2)
    print("Ratio:", tt2 / tt1)


def argmax(arr: Generator[int, None, None]) -> int:
    "Returns index of maximum value in an iterable"
    maxnum: int = next(arr)  # raises StopIteration if empty
    maxidx = 1
    for i, num in enumerate(arr, start=2):
        if num > maxnum:
            maxnum = num
            maxidx = i
    return maxidx

def split_data(txt: str, sep: str) -> Generator[str, None, None]:
    wordlist = []
    word = []
    seplist = []
    for c in txt:
        if sep == "\n" and c == "\n":
            if word:
                yield "".join(word)
                word = []
        elif c in sep:
            seplist.append(c)
            if "".join(seplist) == sep:
                seplist = []
                if wordlist:
                    yield "\n".join(wordlist)
                    word = []
                    wordlist = []
                elif word:
                    wordlist.append("".join(word))
                    word = []
            else:
                wordlist.append("".join(word))
                word = []
        else:
            seplist = []
            word.append(c)
    if wordlist:
        yield "\n".join(wordlist)
    elif word:
        yield "".join(word)

def sum_elf_calories(cals: str) -> int:
    # return sum(int(i) for i in cals.split())
    # data = split_data(cals, sep="\n")
    data = cals.split("\n")
    arr = (int(i) for i in data)
    return sum(arr)


def find_most_calories(data: Generator[str, None, None], n: int = 1) -> int:
    "Gets the sum of calories of n elves"
    # arr = split_data(txt, "\n\n")
    arr = (sum_elf_calories_from_gen(val) for val in data)
    maxnum = 0
    maxidx = 0
    for idx, val in enumerate(data):
        nsum = 0
        if val == '':
            if nsum > maxnum:
                maxnum = nxum
                maxidx = idx
        else:
    if n == 1:
        return max(arr)
    else:
        topn = [next(arr) for _ in range(n)]
        for val1 in arr:
            # find min value in topn
            idxmin = 0
            minval = topn[idxmin]
            for i2, val2 in enumerate(topn[1:], start=1):
                if val2 < minval:
                    idxmin = i2
                    minval = val2
            if val1 > minval:
                topn[idxmin] = val1
        return sum(topn)


def read_data():
    with open("../data.txt") as f:
        while line := f.readline():
            yield line.strip()

def main():
    data = read_data()
    idx = find_most_calories(data, n=3)
    print("Elf with most calories: #", idx, sep="\n")



if __name__ == "__main__":
    timeit(main)
    # print(list(read_data())[:100])
