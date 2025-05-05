N, *S = open(0).read().split()

for i in range(len(S) - 2):
    if S[i] == S[i + 1] == "sweet":
        print("No")
        exit()
print("Yes")
