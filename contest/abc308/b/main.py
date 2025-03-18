from collections import defaultdict


N, M = [int(x) for x in input().split()]
C = input().split()
D = input().split()
P = [int(x) for x in input().split()]

prices = defaultdict(lambda: P[0])
for i in range(M):
    prices[D[i]] = P[i + 1]

ans = sum([prices[c] for c in C])
print(ans)
