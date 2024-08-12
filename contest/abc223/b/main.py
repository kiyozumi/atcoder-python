S = input()
N = len(S)
ans = []

for i in range(N):
    # print(S[i:N] + S[0:i])
    ans.append(S[i:N] + S[0:i])

print(min(ans))
print(max(ans))
