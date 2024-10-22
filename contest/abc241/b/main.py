from collections import defaultdict

N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

d = defaultdict(int)
for a in A:
    d[a] += 1

for b in B:
    if d[b] > 0:
        d[b] -= 1
    else:
        print("No")
        exit()

print("Yes")
