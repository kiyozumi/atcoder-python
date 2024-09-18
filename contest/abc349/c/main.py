S = list(input())
T = list(input().lower())
if T[-1] == "x":
    T = T[:-1]
count = 0
i = 0
for t in T:
    while i < len(S):
        if S[i] == t:
            count += 1
            i += 1
            break
        i += 1


if count == len(T):
    print("Yes")
else:
    print("No")
