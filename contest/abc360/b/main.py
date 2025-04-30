S, T = input().split()

for w in range(1, len(S)):
    splited_S = [S[i : i + w] for i in range(0, len(S), w)]
    for c in range(w):
        ans = "".join([s[c] for s in splited_S if c < len(s)])
        if ans == T:
            print("Yes")
            exit()
print("No")
