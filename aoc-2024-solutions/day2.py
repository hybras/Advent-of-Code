from aocp import *
from collections import Counter
def safe(report: list[int]) -> bool:
    report = report if report[0] < report[1] else report[::-1]
    diffs = [report[i] - report[i-1] for i in range(1,len(report))]
    dif = range(1,4)
    return all([d in dif for d in diffs])

def damp_safe(report: list[int]) -> bool:
    splices = [report[:i] + report[i+1:] for i in range(len(report))]
    return any(map(safe, splices))

def main():
    reports = []
    # Read input
    with open("./input/day2.txt") as f:
        reports = [list(map(int, line.split())) for line in f]

    # part 1
    print(f"Safe reports: {sum(map(safe, reports))}")

    # part 2
    print(f"Damped Safe reports: {sum(map(damp_safe, reports))}")
    

if __name__ == "__main__":
    main()