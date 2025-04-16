N = int(input())
H = [int(x) for x in input().split()]

ans = -1
for i, h in enumerate(H[1:]):
    if H[0] < h:
        ans = i + 2
        break

print(ans)
