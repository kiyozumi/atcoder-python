A, B, K = [int(x) for x in input().split()]

ans = 0
while A < B:
    A *= K
    ans += 1
print(ans)
