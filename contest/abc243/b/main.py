from collections import defaultdict

N = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

d = defaultdict(bool)
for a in A:
    d[a] = True
ans_1 = 0
for a, b in zip(A, B):
    if a == b:
        ans_1 += 1
        del d[a]
print(ans_1)

ans_2 = 0
for b in B:
    if d[b]:
        ans_2 += 1
print(ans_2)
