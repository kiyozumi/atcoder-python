S = input()
T = input()

diff = (ord(S[0]) - ord(T[0])) % 26
for i in range(1, len(S)):
    if diff != (ord(S[i]) - ord(T[i])) % 26:
        print("No")
        exit()
print("Yes")
