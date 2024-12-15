ans = 0

grid = []
with open("input.txt") as file:
    for line in file:
        l = line.strip()
        grid.append([x for x in list(l)])

ans = 0

def inGrid(i,j):
    return i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0])

vis = set()
localVis = set()
cross = set()

def dfs(i, j, cur):
    if (i,j) in localVis:
        return -1
    if not inGrid(i,j):
        return 0
    if grid[i][j] != cur:
        return 0
    
    localVis.add((i,j))
    vis.add((i,j))

    ans = 4

    for di,dj in [[0,1],[1,0],[-1,0],[0,-1]]:
        ni = i + di
        nj = j + dj
        if inGrid(ni,nj) and (ni,nj) in localVis and grid[ni][nj] == cur:
            ans -= 1
            
        if not inGrid(ni,nj) or grid[ni][nj] != cur:
            if abs(di) != 0:
                cross.add((i, (di,dj)))
            if abs(dj) != 0:
                cross.add((j, (di,dj)))

        ans += dfs(i + di, j + dj, cur)
    
    return ans

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i,j) not in vis:
            localVis = set()
            cross =set()
            x = dfs(i,j, grid[i][j])
            ans += x * len(localVis)
            print(grid[i][j], len(localVis), len(cross))

print(ans)