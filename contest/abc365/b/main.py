import numpy as np

N = int(input())
A = [int(x) for x in input().split()]


i = np.argmax(A)
A[i] = 0
print(np.argmax(A) + 1)
