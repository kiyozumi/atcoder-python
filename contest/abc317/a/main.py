N, H, X = [int(x) for x in input().split()]
P = [int(x) for x in input().split()]
for i in range(N):
    if (H + P[i]) >= X:
        print(i + 1)
        exit()
