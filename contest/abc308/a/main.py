S = [int(x) for x in input().split()]

if S == [x for x in sorted(S) if 100 <= x <= 675 and x % 25 == 0]:
    print("Yes")
else:
    print("No")
