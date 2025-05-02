N, T, P = [int(x) for x in input().split()]
L = [int(x) for x in input().split()]

target = sorted(L, reverse=True)[:P]
ans = T - min(target)
print(ans) if ans > 0 else print(0)
