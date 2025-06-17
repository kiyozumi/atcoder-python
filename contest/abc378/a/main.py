A = [int(x) for x in input().split()]

ans = sum(A.count(n) // 2 for n in range(1, 5))
print(ans)
