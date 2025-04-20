N = int(input())
S = input()

ans = S.find("ABC")
print(ans + 1) if ans >= 0 else print(-1)
