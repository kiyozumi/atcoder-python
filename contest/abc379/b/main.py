N, K = [int(x) for x in input().split()]
S = input()

ans = sum(len(x) // K for x in S.split("X"))
print(ans)
