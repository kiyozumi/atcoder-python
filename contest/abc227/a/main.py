N, K, A = [int(x) for x in input().split()]
ans = (K + A - 1) % N
print(N) if ans == 0 else print(ans)
