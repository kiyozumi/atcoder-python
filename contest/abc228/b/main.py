N, X = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
i = X
ans = set()
ans.add(X)
for _ in range(N):
    i = A[i - 1]
    if i in ans:
        break
    ans.add(i)

print(len(ans))
