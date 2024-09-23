N = int(input())
A = [int(x) for x in input().split()]

B = [0] * (N + 1)
head = 0
for i, a in enumerate(A):
    if a == -1:
        head = i + 1
    else:
        B[a] = i + 1

ans = [head]
x = head
for _ in range(N - 1):
    ans.append(B[x])
    x = B[x]

print(*ans)
