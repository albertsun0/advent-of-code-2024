ans = 0

grid = []
with open("input.txt") as file:
    for line in file:
        l = line.strip()
        grid.append([int(x) for x in list(l)])

# dfs for part 1 using global vis
vis = set()
def dfs(r,c):
    cur = grid[r][c]
    if (r,c) in vis:
        return 0
    vis.add((r,c))
    if grid[r][c] == 9:
        return 1
    ans = 0
    for dr,dc in [[0,1],[0,-1],[1,0],[-1,0]]:
        nr = r + dr
        nc = c + dc
        if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and grid[nr][nc] == cur + 1:
            ans += dfs(nr,nc)

    return ans

# dfs for part 2 using local vis (setting grid vals)
def dfs2(r,c):
    cur = grid[r][c]
    if grid[r][c] == -1:
        return 0
    if grid[r][c] == 9:
        return 1
    grid[r][c] = -1
    ans = 0
    for dr,dc in [[0,1],[0,-1],[1,0],[-1,0]]:
        nr = r + dr
        nc = c + dc
        if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and grid[nr][nc] == cur + 1:
            ans += dfs2(nr,nc)
    grid[r][c] = cur
    return ans

ans = 0

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 0:
            # vis = set()
            ans += dfs2(i,j)

print(ans)