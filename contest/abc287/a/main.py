N = int(input())

y, n = 0, 0
for _ in range(N):
    S = input()
    if S == "For":
        y += 1
    else:
        n += 1

print("Yes" if y > n else "No")
