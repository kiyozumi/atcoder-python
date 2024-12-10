X, Y, Z = [int(x) for x in input().split()]

if Y < 0:
    X = -X
    Y = -Y
    Z = -Z

if X < Y:
    print(abs(X))
else:
    if Z > Y:
        print(-1)
    else:
        print(abs(Z) + abs(X - Z))
