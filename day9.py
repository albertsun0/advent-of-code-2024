ans = 0

input = []
with open("input.txt") as file:
    for line in file:
        l = line.strip()
        input = [int(x) for x in list(l)]

index = 0

# simulate using free and taken blocks
blocks = []
free = []
count = 0

for i in range(len(input)):
    if i % 2 == 0:
        add = index
        blocks.append([count, count + input[i] - 1, index])
        index += 1
    else:
        free.append([count, count + input[i] - 1])
    count += input[i]

blocks.sort(reverse=True)

# for each block, find first free position it can fit in
# reduce free block by that amount
for i in range(len(blocks)):
    s, e, id = blocks[i]
    block_len = e - s + 1
    for j in range(len(free)):
        a, b = free[j]
        if a > s:
            break
        diff = b - a + 1
        if diff >= block_len:
            blocks[i] = [a, a + block_len - 1, id]
            free[j] = [a + block_len, b]
            break

ans = 0

for s, e, id in blocks:
    for i in range(s, e + 1):
        ans += i * id

print(ans)
