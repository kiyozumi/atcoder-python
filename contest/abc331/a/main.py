M, D = [int(x) for x in input().split()]
y, m, d = [int(x) for x in input().split()]

if d < D:
    d += 1
else:
    d = 1
    if m + 1 < M:
        m += 1
    else:
        m = 1
        y += 1

print(y, m, d)
