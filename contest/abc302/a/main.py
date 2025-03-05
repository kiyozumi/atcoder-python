A, B = [int(x) for x in input().split()]

ans = A // B if A % B == 0 else (A // B) + 1
print(ans)
