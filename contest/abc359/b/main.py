N = int(input())
A = [int(x) for x in input().split()]

ans = 0
for i in range(N):
    l = A.index(i + 1)
    if A[l] == A[l + 1]:
        continue
    if A[l] == A[l + 2]:
        ans += 1
print(ans)
