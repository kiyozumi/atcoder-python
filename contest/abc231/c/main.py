import bisect

N, Q = [int(x) for x in input().split()]
A = sorted([int(x) for x in input().split()])

for _ in range(Q):
    X = int(input())
    idx = bisect.bisect_left(A, X)
    # print(len(A[idx:]))
    print(N - idx)
