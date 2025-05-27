M = int(input())

A = []
for k in range(11):
    M, r = divmod(M, 3)
    A.extend([k] * r)

print(len(A))
print(*A)
