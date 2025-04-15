S = input()
T = input()
ans = []
idx = 0
for i, t in enumerate(T):
    if S[idx] == t:
        ans.append(i + 1)
        idx += 1

print(*ans)
