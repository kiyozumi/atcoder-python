S = list(input())
T = list(input())

if S == T:
    print("Yes")
    exit()

for i in range(len(S) - 1):
    S[i], S[i + 1] = S[i + 1], S[i]
    if S == T:
        print("Yes")
        exit()
    S[i], S[i + 1] = S[i + 1], S[i]

print("No")
