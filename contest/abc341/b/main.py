N = int(input())
A = [int(x) for x in input().split()]

for i in range(N - 1):
    S, T = [int(x) for x in input().split()]
    A[i + 1] += (A[i] // S) * T
print(A[-1])
