import re


def part1(crossword: list[str]) -> int:
    total = 0
    length = len(crossword)
    dirs = [
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        [(0, 0), (1, 1), (2, 2), (3, 3)],
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(0, 0), (1, -1), (2, -2), (3, -3)],
        [(0, 0), (0, -1), (0, -2), (0, -3)],
        [(0, 0), (-1, -1), (-2, -2), (-3, -3)],
        [(0, 0), (-1, 0), (-2, 0), (-3, 0)],
        [(0, 0), (-1, 1), (-2, 2), (-3, 3)],
    ]
    xmas = list("XMAS")
    for x in range(length):
        for y in range(length):
            if crossword[x][y] == "X":
                for d in dirs:
                    dx, dy = d[3]
                    if 0 <= x + dx < length and 0 <= y + dy < length:
                        view = [crossword[x + dx][y + dy] for dx, dy in d]
                        if view == xmas:
                            total += 1
    return total


def part2(crossword: list[str]) -> int:
    total = 0
    length = len(crossword)
    dirs = [
        [(-1, 1), (0, 0), (1, -1)],
        [(1, -1), (0, 0), (-1, 1)],
        [(1, 1), (0, 0), (-1, -1)],
        [(-1, -1), (0, 0), (1, 1)],
    ]
    mas = list("MAS")

    for x in range(1, length-1):
        for y in range(1, length-1):
            if crossword[x][y] == "A":
                loc_total = 0
                for d in dirs:
                    view = [crossword[x + dx][y + dy] for dx, dy in d]
                    if view == mas:
                        loc_total += 1
                if loc_total == 2:
                    total += 1
    return total


def main():
    # Read input
    crossword = open("./input/day4.txt").readlines()

    # part 1
    print(f"Total: {part1(crossword)}")

    # part 2
    print(f"Cond Total: {part2(crossword)}")


if __name__ == "__main__":
    main()
