N, K = [int(x) for x in input().split()]
A = sorted(set([int(x) for x in input().split()]))
A = [x for x in A if x <= K]
sumk = int((K * (K + 1)) // 2)
print(sumk - sum(A))
