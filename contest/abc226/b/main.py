N = int(input())
A = [[int(x) for x in input().split()] for _ in range(N)]
ans = set()
for a in A:
    ans.add(tuple(a))
print(len(ans))
