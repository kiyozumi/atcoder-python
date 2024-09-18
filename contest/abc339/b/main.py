H, W, N = [int(x) for x in input().split()]
grid = []
for _ in range(H):
    grid.append('.' * W)
i, j = 0, 0
for n in range(N):
    match grid[i][j]:
        case '.':
            print(grid[i][j])
            grid[i][j] = '#'
        case '#':
            print(grid[i][j])
            grid[i][j] = '.'

for row in grid:
    print(row)

