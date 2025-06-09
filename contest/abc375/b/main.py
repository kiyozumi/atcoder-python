import math


N = int(input())

ans = 0
x, y = 0, 0
for i in range(N):
    X, Y = [int(x) for x in input().split()]
    ans += math.hypot(x - X, y - Y)
    x, y = X, Y
ans += math.hypot(x - 0, y - 0)
print(ans)
