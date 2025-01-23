N, M = [int(x) for x in input().split()]
S = [input() for _ in range(N)]
T = {}
for _ in range(M):
    T[input()] = True

ans = 0
for s in S:
    if T.get(s[-3:]):
        ans += 1

print(ans)
