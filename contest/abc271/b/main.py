N, Q = [int(x) for x in input().split()]
A = [[int(x) for x in input().split()] for _ in range(N)]

for i in range(Q):
    i, j = [int(x) for x in input().split()]
    print(A[i - 1][j])
