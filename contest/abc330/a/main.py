N, L = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

ans = [x for x in A if x >= L]
print(len(ans))
