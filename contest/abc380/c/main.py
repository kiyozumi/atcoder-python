from itertools import groupby


N, K = [int(x) for x in input().split()]
S = ["".join(group) for key, group in groupby(input())]
k = 0
for i, s in enumerate(S):
    if "1" in s:
        k += 1
        if k == K:
            S[i - 1], S[i] = S[i], S[i - 1]
            break
print("".join(S))
