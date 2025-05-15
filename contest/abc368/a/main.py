N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

ans = A[-K:] + A[:-K]
print(*ans)
