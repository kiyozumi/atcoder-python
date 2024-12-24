N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

for _ in range(K):
    A.append(0)
print(*A[K:])
