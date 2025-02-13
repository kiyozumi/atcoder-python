N, D = [int(x) for x in input().split()]
T = [int(x) for x in input().split()]

ans = -1
for i in range(1, N):
    if T[i] - T[i - 1] <= D:
        ans = T[i]
        break
print(ans)
