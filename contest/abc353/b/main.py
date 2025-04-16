N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

ans, k = 0, 0
for a in A:
    if k + a <= K:
        k += a
    else:
        ans += 1
        k = a
print(ans + 1)
