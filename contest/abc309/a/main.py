A, B = [int(x) for x in input().split()]

if (B - A) == 1 and A % 3 in (1, 2):
    print("Yes")
else:
    print("No")
