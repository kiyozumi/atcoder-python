A, B = [int(x) for x in input().split()]
for i in range(0, 10):
    if (A + B) != i:
        print(i)
        exit()
