N = input()

if len(N) <= 3:
    print(N)
else:
    zero = "0" * (len(N) - 3)
    print(N[:3] + zero)
