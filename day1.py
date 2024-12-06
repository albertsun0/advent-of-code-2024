from sys import stdin, stdout
from collections import defaultdict


def readintln():
    return [int(x) for x in stdin.readline().split()]


left = []
d = defaultdict(int)

with open("input.txt") as file:
    for line in file:
        a, b = [int(x) for x in line.split()]
        left.append(a)
        d[b] += 1

left.sort()


ans = 0
for a in left:
    ans += a * d[a]

print(ans)
