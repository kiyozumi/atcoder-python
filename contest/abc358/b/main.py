N, A = [int(x) for x in input().split()]
T = [int(x) for x in input().split()]

ans = 0
for t in T:
    ans = max(ans, t) + A
    print(ans)
