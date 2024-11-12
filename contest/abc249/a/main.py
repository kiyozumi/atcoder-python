def calc(n1: int, n2: int, n3: int, x: int) -> int:
    q = x // (n1 + n3)
    r = x % (n1 + n3)
    return (q * n1 + min(r, n1)) * n2


A, B, C, D, E, F, X = [int(x) for x in input().split()]

takahashi = calc(A, B, C, X)
aoki = calc(D, E, F, X)

if takahashi > aoki:
    print("Takahashi")
elif aoki > takahashi:
    print("Aoki")
else:
    print("Draw")
