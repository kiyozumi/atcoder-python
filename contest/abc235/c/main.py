from collections import defaultdict

N, Q = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

d = defaultdict(list)
for i, n in enumerate(a, start=1):
    d[n].append(i)

for _ in range(Q):
    x, k = [int(x) for x in input().split()]
    l = d[x]
    if k > len(l):
        print(-1)
    else:
        print(l[k - 1])
