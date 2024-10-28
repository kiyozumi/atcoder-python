A, B, C, D = [int(x) for x in input().split()]

takahashi = 60 * A + B
aoki = 60 * C + D
if takahashi <= aoki:
    print("Takahashi")
else:
    print("Aoki")
