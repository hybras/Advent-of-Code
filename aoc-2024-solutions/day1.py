from aocp import *
from collections import Counter

def main():
    xs = []
    ys = []
    # Read input
    with open("./input/day1.txt") as f:
        for line in f:
            # split line into two ints
            [x, y] = line.split()
            xs.append(int(x))
            ys.append(int(y))


    # part 1
    xs.sort()
    ys.sort()
    diffs = [abs(x - y) for x,y in zip(xs, ys)]
    diff = sum(diffs)
    print(f"Diff: {diff}")

    # part 2
    x_set = set(xs)
    y_counts = Counter(ys)
    similarity_score = sum([
        x * y_counts[x] 
        for x in x_set.intersection(y_counts.keys())
        ])

    print(f"Similarity score: {similarity_score}")

if __name__ == "__main__":
    main()
    