N, X, Y, Z = [int(x) for x in input().split()]

if X <= Z <= Y or Y <= Z <= X:
    print("Yes")
else:
    print("No")
