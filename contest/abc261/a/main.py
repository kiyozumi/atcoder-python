L1, R1, L2, R2 = [int(x) for x in input().split()]
print(max(0, min(R1, R2) - max(L1, L2)))
