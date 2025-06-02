S = input()

cur_idx = S.index("A")
ans = 0
for c in "BCDEFGHIJKLMNOPQRSTUVWXYZ":
    next_idx = S.index(c)
    ans += abs(next_idx - cur_idx)
    cur_idx = next_idx
print(ans)
