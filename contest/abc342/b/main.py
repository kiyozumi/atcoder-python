N = int(input())
P = [int(x) for x in input().split()]
Q = int(input())

d = {}
for i, p in enumerate(P):
    d[p] = i + 1

for _ in range(Q):
    a, b = [int(x) for x in input().split()]
    a_idx = d.get(a)
    b_idx = d.get(b)
    print(a) if a_idx < b_idx else print(b)
