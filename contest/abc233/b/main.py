L, R = [int(x) for x in input().split()]
S = input()
L = L - 1
rs = S[L:R][::-1]
print(S[:L] + rs + S[R:])
