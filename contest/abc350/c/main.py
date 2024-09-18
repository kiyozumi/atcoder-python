N = int(input())
A = [int(x) for x in input().split()]

ans = []

for i in range(N):
    while A[i] != i + 1:
        x = A[i]
        ans.append((i + 1, x))
        A[i], A[x - 1] = A[x - 1], A[i]


print(len(ans))
for a in ans:
    print(*a)
