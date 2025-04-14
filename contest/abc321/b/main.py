N, X = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
s = sorted(A)

ans = X - sum(s[:-1])
if ans <= 0:
    print(0)
    exit()

ans = X - sum(s[1:-1])
if ans <= s[-1]:
    print(ans)
else:
    print(-1)
