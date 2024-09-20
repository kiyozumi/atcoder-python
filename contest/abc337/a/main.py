N = int(input())
xsum = 0
ysum = 0
for _ in range(N):
    X, Y = [int(x) for x in input().split()]
    xsum += X
    ysum += Y

if xsum > ysum:
    print("Takahashi")
elif xsum < ysum:
    print("Aoki")
else:
    print("Draw")
