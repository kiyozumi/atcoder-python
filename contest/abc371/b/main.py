N, M = [int(x) for x in input().split()]

d = {}
for i in range(M):
    A, B = input().split()
    if B == "M" and not d.get(A):
        d[A] = B
        print("Yes")
    else:
        print("No")
