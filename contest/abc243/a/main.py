V, A, B, C = [int(x) for x in input().split()]

V %= A + B + C
if V < A:
    print("F")
elif V < A + B:
    print("M")
else:
    print("T")
