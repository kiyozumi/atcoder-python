H, W = [int(x) for x in input().split()]

indexes = []
for r in range(H):
    s = list(input())
    for c in range(W):
        if s[c] == "o":
            indexes.append((r, c))

a, b = indexes[0]
c, d = indexes[1]
print(abs(a - c) + abs(b - d))
