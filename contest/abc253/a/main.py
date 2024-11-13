l = [int(x) for x in input().split()]
b = l[1]
if b == sorted(l)[1]:
    print("Yes")
else:
    print("No")
