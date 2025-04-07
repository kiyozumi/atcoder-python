N, M, P = [int(x) for x in input().split()]
print(0) if N < M else print((N - M) // P + 1)
