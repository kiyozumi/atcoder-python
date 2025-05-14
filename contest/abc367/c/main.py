import itertools

N, K = [int(x) for x in input().split()]
R = [int(x) for x in input().split()]

patterns = (range(1, r + 1) for r in R)
for l in itertools.product(*patterns):
    if sum(l) % K == 0:
        print(*l)
