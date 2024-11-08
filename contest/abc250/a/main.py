H, W = [int(x) for x in input().split()]
R, C = [int(x) for x in input().split()]

ans = 0

if R != 1:
    ans += 1
if R != H:
    ans += 1
if C != 1:
    ans += 1
if C != W:
    ans += 1

print(ans)
