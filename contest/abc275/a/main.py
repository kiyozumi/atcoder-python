N = int(input())
H = [int(x) for x in input().split()]
ans = H.index(max(H)) + 1
print(ans)
