A, B = [int(x) for x in input().split()]

if A - B == 0:
    print(1)
    exit()

if (A - B) % 2 == 0:
    print(3)
else:
    print(2)
