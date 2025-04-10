S = input()

ans = 1
for i in range(len(S)):
    for j in range(i + 1, len(S) + 1):
        substring = S[i:j]
        if substring == substring[::-1]:
            ans = max(len(substring), ans)

print(ans)
