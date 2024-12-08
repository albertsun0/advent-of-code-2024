from collections import defaultdict

ans = 0

grid = []
with open("input.txt") as file:
    for line in file:
        l = line.strip()
        grid.append(l)

# set/grid of antinodes
count = [[0] * len(grid[0]) for i in range(len(grid))]

d = defaultdict(list)

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] != ".":
            d[grid[i][j]].append([i, j])


def inGrid(r, c):
    return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])


for item in d:
    positions = d[item]
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            x1, y1 = positions[i]
            x2, y2 = positions[j]

            dx = x1 - x2
            dy = y1 - y2
            for x in [1, -1]:
                nx = x1
                ny = y1
                while inGrid(nx, ny):
                    count[nx][ny] = 1
                    nx = nx + dx * x
                    ny = ny + dy * x


ans = sum([sum(x) for x in count])

print(ans)
