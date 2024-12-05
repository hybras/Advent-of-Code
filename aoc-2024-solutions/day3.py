import re

def part1(memory: str) -> int:
    mul_pat = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    matches = mul_pat.finditer(memory)
    total = sum([int(x) * int(y) for (x, y) in matches])
    return total

def part2(memory: str) -> None:
    memory = "do()" + memory
    do_pat = re.compile(r"do\(\)")
    dont_pat = re.compile(r"don't\(\)")
    mul_pat = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    sections = [dont_pat.split(section, maxsplit=1)[0] for section in do_pat.split(memory)]
    return sum(map(part1, sections))


def main():
    # Read input
    memory = open("./input/day3.txt").read()

    # part 1
    print(f"Total: {part1(memory)}")

    # part 2
    print(f"Cond Total: {part2(memory)}")

if __name__ == "__main__":
    main()