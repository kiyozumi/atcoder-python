import itertools

S = list(input())
ans = set(itertools.permutations(S))
print(len(ans))
