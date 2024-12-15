stones = []

with open("input.txt") as file:
    for line in file:
        l = line.strip()
        stones = [int(x) for x in l.split()]



def multiply(start):
    stones = [start]
    for i in range(75):
        n = []
        for stone in stones:
            s = str(stone)
            if stone == 0:
                n.append(1)
            elif len(s) % 2 == 0:
                n.append(int(s[0:len(s)//2]))
                n.append(int(s[len(s)//2:]))
            else:
                n.append(stone * 2024)
        stones = n
    return len(stones)

cur = stones

ans = 0
for stone in stones:
    print(stone)
    ans += multiply(stone)

print(ans)

# 0 -> 1
# even -> 2
# else -> even