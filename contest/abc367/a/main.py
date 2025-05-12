A, B, C = [int(x) for x in input().split()]

if B <= C:
    if B <= A <= C:
        print("No")
        exit()
else:
    if B <= A or A <= C:
        print("No")
        exit()

print("Yes")
