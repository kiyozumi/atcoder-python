import numpy as np


N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
X = [[int(x) for x in input().split()] for _ in range(N)]

column_sums = np.array(X).sum(axis=0)
if all(cs >= a for cs, a in zip(column_sums, A)):
    print("Yes")
else:
    print("No")
