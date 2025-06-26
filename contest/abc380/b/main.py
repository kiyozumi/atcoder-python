S = input()

ans = []
for a in S.split("|"):
    if a:
        ans.append(len(a))
print(*ans)
