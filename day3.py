from sys import stdin
import re


def readintln():
    return [int(x) for x in stdin.readline().split()]


ans = 0

with open("input.txt") as file:
    for line in file:
        matches = re.findall(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))", line)
        mult = True
        # not exactly sure what is wrong with this regex
        for match in matches:
            if match == "do()":
                mult = True
            elif match == "don't()":
                mult = False
            elif mult:
                sp = match.split(",")
                a = sp[0].strip("mul()")
                b = sp[1].strip("mul()")
                ans += int(a) * int(b)
print(ans)
