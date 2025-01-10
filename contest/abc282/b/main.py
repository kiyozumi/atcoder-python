from itertools import combinations

N, M = [int(x) for x in input().split()]
S = [list(input()) for _ in range(N)]

ans = 0
for i1, i2 in combinations([i for i in range(N)], 2):
    for j in range(M):
        if S[i1][j] == "x" and S[i2][j] == "x":
            break
    else:
        ans += 1

print(ans)
