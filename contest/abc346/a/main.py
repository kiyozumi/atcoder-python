N = int(input())
A = [int(x) for x in input().split()]
ans = []
for i in range(N - 1):
    B = A[i] * A[i + 1]
    ans.append(B)
print(*ans)
