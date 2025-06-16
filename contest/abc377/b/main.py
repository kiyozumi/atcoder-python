S = [input() for _ in range(8)]

ng_columns = [False] * 8
ans = 0
for s in S:
    if "#" in s:
        for j in range(len(s)):
            if s[j] == "#":
                ng_columns[j] = True
    else:
        ans += 1
print(ans * ng_columns.count(False))
