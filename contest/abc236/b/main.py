from collections import Counter

N = int(input())
A = [int(x) for x in input().split()]
c = Counter(A)
print(min(c, key=c.get))
