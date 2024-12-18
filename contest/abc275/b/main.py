A, B, C, D, E, F = [int(x) for x in input().split()]
ans = (A * B * C - D * E * F) % 998244353
print(ans)
