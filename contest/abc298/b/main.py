import numpy as np


N = int(input())
A = np.array([[int(x) for x in input().split()] for _ in range(N)])
B = np.array([[int(x) for x in input().split()] for _ in range(N)])

for _ in range(4):
    if np.min(B - A) >= 0:
        print("Yes")
        exit()
    else:
        A = np.rot90(A)
print("No")
