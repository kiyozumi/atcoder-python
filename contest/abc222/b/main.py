N, P = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]

ans = [x for x in a if x < P]
print(len(ans))
