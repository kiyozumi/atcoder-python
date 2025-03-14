A = [int(x) for x in input().split()]
ans = sum([2**i for i, x in enumerate(A) if x == 1])
print(ans)
