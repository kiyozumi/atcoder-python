N = int(input())
A = set([int(x) for x in input().split()])

s = sorted(A, reverse=True)
print(s[1])
