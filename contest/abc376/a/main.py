N, C = [int(x) for x in input().split()]
T = [int(x) for x in input().split()]

ans = 1
c = T[0]
for t in T[1:]:
    if t - c >= C:
        ans += 1
        c = t
print(ans)
