N = int(input())
A = [[int(x) for x in input().split()] for _ in range(N)]

ans = 0
for i in range(N):
    if ans >= i:
        ans = A[ans][i]
    else:
        ans = A[i][ans]
    ans -= 1
print(ans + 1)
