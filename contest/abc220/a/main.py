A, B, C = [int(x) for x in input().split()]

ans = B // C * C
if A <= ans:
    print(ans)
else:
    print(-1)
