N, K, Q = [int(x) for x in input().split()]
L = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

grid = [0] * N
for l in L:
    grid[l - 1] = 1

for a in A:
    l = L[a - 1] - 1
    if l < N - 1:
        if grid[l + 1] == 0:
            grid[l] = 0
            grid[l + 1] = 1
            L[a - 1] += 1
print(*L)
