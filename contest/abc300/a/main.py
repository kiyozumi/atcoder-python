N, A, B = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]
ans = C.index(A + B) + 1
print(ans)
