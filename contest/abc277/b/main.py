N = int(input())
l = set()
for _ in range(N):
    S = input()
    if S[0] not in ("H", "D", "C", "S"):
        print("No")
        exit()
    if S[1] not in ("A", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K"):
        print("No")
        exit()
    l.add(S)

print("Yes") if len(l) == N else print("No")
