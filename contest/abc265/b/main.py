N, M, T = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [[int(x) for x in input().split()] for _ in range(M)]

d = {}
for x, y in B:
    d[x] = y

for i, a in enumerate(A):
    T -= a
    T += d.get(i + 1, 0)
    if T <= 0:
        print("No")
        exit()
print("Yes")
