H, W = [int(x) for x in input().split()]
Si, Sj = [int(x) - 1 for x in input().split()]
C = [input() for _ in range(H)]
X = input()

for x in X:
    match (x):
        case "U":
            if Si - 1 >= 0 and C[Si - 1][Sj] == ".":
                Si -= 1
        case "R":
            if Sj + 1 < W and C[Si][Sj + 1] == ".":
                Sj += 1
        case "D":
            if Si + 1 < H and C[Si + 1][Sj] == ".":
                Si += 1
        case "L":
            if Sj - 1 >= 0 and C[Si][Sj - 1] == ".":
                Sj -= 1
print(Si + 1, Sj + 1)
