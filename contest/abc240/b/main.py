from collections import Counter

N, *a = [int(x) for x in open(0).read().split()]
print(len(Counter(a)))
