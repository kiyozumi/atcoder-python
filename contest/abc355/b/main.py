N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

C = sorted(A + B)
count = 0
for c in C:
    if c in A:
        count += 1
    else:
        count = 0

    if count >= 2:
        print("Yes")
        exit()
print("No")
