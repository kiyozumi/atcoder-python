N = int(input())
A = [int(x) for x in input().split()]

ans = []
for i in range(1, N):
    c = 1 if A[i] - A[i - 1] >= 0 else -1
    ans += list(range(A[i - 1], A[i], c))
ans.append(A[-1])
print(*ans)
