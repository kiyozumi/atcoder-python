from collections import Counter

N, *S = open(0).read().split()
name, frequency = Counter(S).most_common(1)[0]
print(name)
