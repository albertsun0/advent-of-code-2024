ans = 0
grid = []
with open("input.txt") as file:
    for line in file:
        grid.append(line.strip())

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

t = [len(x) for x in grid]


# search for word in direction
def search(r, c, word, dir):
    for i in word:
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[r]):
            return False
        if i != grid[r][c]:
            return False
        r += dirs[dir][0]
        c += dirs[dir][1]
    return True


def inGrid(r, c):
    return r >= 0 and r < len(grid) and c >= 0 and c < len(grid[r])


def search2(r, c):
    # middle character must be A
    if grid[r][c] != "A":
        return False
    # Diagonals must contain M and S
    d = [[[-1, -1], [1, 1]], [[-1, 1], [1, -1]]]
    for group in d:
        s = set()
        for dr, dc in group:
            if not inGrid(r + dr, c + dc):
                return False
            s.add(grid[r + dr][c + dc])
        if not ("M" in s and "S" in s):
            return False

    return True


for i in range(len(grid)):
    for j in range(len(grid[i])):
        if search2(i, j):
            ans += 1

print(ans)
