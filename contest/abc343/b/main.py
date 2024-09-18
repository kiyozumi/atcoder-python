N = int(input())
for _ in range(N):
    A = [int(x) for x in input().split()]
    ans = []
    for i, v in enumerate(A):
        if v == 1:
            ans.append(i + 1)
    print(*ans)
