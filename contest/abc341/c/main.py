H, W, N = [int(x) for x in input().split()]
T = input()
S = [input() for _ in range(H)]

ans = 0
for i in range(1, H - 1):
    for j in range(1, W - 1):
        if S[i][j] == "#":
            continue
        x, y = i, j
        ok = True
        for t in T:
            match t:
                case "U":
                    x -= 1
                case "D":
                    x += 1
                case "L":
                    y -= 1
                case "R":
                    y += 1
            if S[x][y] == "#":
                ok = False
                break
        if ok:
            ans += 1

print(ans)
