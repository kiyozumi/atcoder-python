from string import ascii_uppercase

N, X = [int(x) for x in input().split()]
print(ascii_uppercase[(X - 1) // N])
