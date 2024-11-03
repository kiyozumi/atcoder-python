S = "".join(sorted(input()))
T = "".join(sorted(input()))
P = ("AB", "BC", "CD", "DE", "AE")

if (S in P) == (T in P):
    print("Yes")
else:
    print("No")
