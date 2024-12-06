from sys import stdin, stdout
from collections import defaultdict


def readintln():
    return [int(x) for x in stdin.readline().split()]


def check(x):
    if x[0] > x[1]:
        # decreasing
        for i in range(1, len(x)):
            diff = x[i - 1] - x[i]
            if diff < 1 or diff > 3:
                return False
    else:
        # increase
        for i in range(1, len(x)):
            diff = x[i] - x[i - 1]
            if diff < 1 or diff > 3:
                return False

    return True


ans = 0

with open("input.txt") as file:
    for line in file:
        l = [int(x) for x in line.split()]
        for i in range(len(l)):
            # brute force to remove one element from the list
            nl = l[:i] + l[i + 1 :]
            if check(nl):
                ans += 1
                break

print(ans)
