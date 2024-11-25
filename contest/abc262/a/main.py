Y = int(input())

if Y % 4 <= 2:
    print(2 - (Y % 4) + Y)
else:
    print((Y % 4) + Y)
