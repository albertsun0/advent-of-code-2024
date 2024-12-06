grid = []

with open("input.txt") as file:
    for line in file:
        l = line.strip()
        grid.append(list(l))

r = 0
c = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "^":
            r = i
            c = j

ans = 0
vis = set()

dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def canEscape(grid):
    cr = r
    cc = c
    dir = 0

    def inGrid(r, c):
        return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[0])

    vis = set()

    while inGrid(cr, cc):
        if (cr, cc, dir) in vis:
            return False

        vis.add((cr, cc, dir))
        nr = cr + dirs[dir][0]
        nc = cc + dirs[dir][1]

        if not inGrid(nr, nc):
            return True

        if grid[nr][nc] == "#":
            dir = (dir + 1) % 4
        else:
            cr = nr
            cc = nc

    return True


# slow brute force (~30 sec)
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == ".":
            grid[i][j] = "#"
            if not canEscape(grid):
                ans += 1
            grid[i][j] = "."

print(ans)
