N, *A = [int(x) for x in open(0).read().split()]

P = 0
grid = [False] * 4

for a in A:
    next_grid = [False] * 4
    grid[0] = True
    for i in range(len(grid)):
        if grid[i]:
            if i + a >= len(grid):
                P += 1
            else:
                next_grid[i + a] = True
    grid = next_grid
print(P)
