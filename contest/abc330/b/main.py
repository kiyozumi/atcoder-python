N, L, R = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

ans = []
for a in A:
    if L <= a <= R:
        ans.append(a)
    elif a < L:
        ans.append(L)
    elif a > R:
        ans.append(R)

print(*ans)
