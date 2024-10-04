X, Y = [int(x) for x in input().split()]
diff = Y - X
if diff <= 0:
    print(0)
else:
    print((diff + 10 - 1) // 10)
