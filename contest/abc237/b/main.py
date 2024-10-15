(H, W), *A = [[int(x) for x in s.split()] for s in open(0)]

B = [list(x) for x in zip(*A)]
for b in B:
    print(*b)
