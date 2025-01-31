N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

ans = 0
for i in B:
    ans += A[i - 1]

print(ans)
