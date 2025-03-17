N = int(input())
A = [int(x) for x in input().split()]

ans = []
for i in range(7, (N * 7) + 1, 7):
    ans.append(sum(A[i - 7 : i]))

print(*ans)
