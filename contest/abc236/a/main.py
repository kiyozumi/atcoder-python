S = list(input())
a, b = [int(x) for x in input().split()]
S[a - 1], S[b - 1] = S[b - 1], S[a - 1]
print("".join(S))
