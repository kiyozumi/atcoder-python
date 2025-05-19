N, *A = [int(x) for x in open(0).read().split()]

print(min(sum(A) // 2, sum(A) - max(A)))
