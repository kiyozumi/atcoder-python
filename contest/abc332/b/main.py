K, G, M = [int(x) for x in input().split()]

g, m = 0, 0
for _ in range(K):
    if g == G:
        g = 0
    elif m == 0:
        m = M
    else:
        available = min(m, G - g)
        g, m = g + available, m - available

print(g, m)
