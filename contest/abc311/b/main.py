N, D = [int(x) for x in input().split()]
S = [input() for _ in range(N)]

ans, c = 0, 0
for d in range(D):
    for n in range(N):
        if S[n][d] != "o":
            c = 0
            break
    else:
        c += 1
        if ans < c:
            ans = c
print(ans)
