N = int(input())
H = [int(x) for x in input().split()]
ans = 0
for h in H:
    if ans < h:
        ans = h
    else:
        break
print(ans)
