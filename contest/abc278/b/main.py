H, M = [int(x) for x in input().split()]

A, B = list(f"{H:02d}")
C, D = list(f"{M:02d}")

if A in ("0", "1"):
    if B in ("6", "7", "8", "9"):
        A = str(int(A) + 1)
        B, C, D = "0", "0", "0"
else:
    if C in ("4", "5"):
        C, D = "0", "0"
        if B == "3":
            A, B = "0", "0"
        else:
            B = str(int(B) + 1)

print(A + B, C + D)
