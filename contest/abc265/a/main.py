X, Y, N = [int(x) for x in input().split()]

if (Y // 3) <= X:
    x = N % 3
    y = N // 3
    print((X * x) + (Y * y))
else:
    print(X * N)
