N, M = [int(x) for x in input().split()]

G = [[] for _ in range(N)]

for _ in range(M):
    A, B = [int(x) for x in input().split()]
    G[A - 1].append(B)
    G[B - 1].append(A)

for g in G:
    g.sort()
    print(len(g), *g)
