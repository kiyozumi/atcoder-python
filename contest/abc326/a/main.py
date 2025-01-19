X, Y = [int(x) for x in input().split()]

move = X - Y
if -2 <= move <= 3:
    print("Yes")
else:
    print("No")
