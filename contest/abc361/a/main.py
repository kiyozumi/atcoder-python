N, K, X = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

ans = A[:K] + [X] + A[K:]
print(*ans)
