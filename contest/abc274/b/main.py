H, W = [int(x) for x in input().split()]

ans = [0] * W
for i in range(H):
    X = input()
    for j in range(W):
        if X[j] == "#":
            ans[j] += 1

print(*ans)
