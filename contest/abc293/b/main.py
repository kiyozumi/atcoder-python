N = int(input())
A = [int(x) for x in input().split()]

B = [False] * N
for i, a in enumerate(A):
    if not B[i]:
        B[a - 1] = True

X = []
for i, b in enumerate(B):
    if not b:
        X.append(i + 1)

print(len(X))
print(*X)
