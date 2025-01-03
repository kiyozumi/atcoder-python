N, X = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]


ans = sum([x for x in A if x <= X])
print(ans)
