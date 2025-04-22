N, L, R = [int(x) for x in input().split()]
A = [x for x in range(1, N + 1)]
A[L - 1 : R] = A[L - 1 : R][::-1]
print(*A)
