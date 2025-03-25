N = int(input())
S = input()

ans = max(S.find("A"), S.find("B"), S.find("C")) + 1
print(ans)
# max(S.find(c)for c in "ABC") + 1
