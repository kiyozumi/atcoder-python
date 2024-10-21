a, b = [int(x) for x in input().split()]

diff = b - a
if diff == 1 or diff == 9:
    print("Yes")
else:
    print("No")
