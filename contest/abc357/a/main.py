N, M = [int(x) for x in input().split()]
H = [int(x) for x in input().split()]

ans = 0
for h in H:
    if M - h >= 0:
        M -= h
        ans += 1
    else:
        break
print(ans)
