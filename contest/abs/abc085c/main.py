N, Y = [int(x) for x in input().split()]

result = [-1, -1, -1]
for i in range(N + 1):
    for j in range(N + 1 - i):
        k = N - i - j
        if i * 10000 + j * 5000 + k * 1000 == Y:
            print(i, j, k)
            exit()

print(-1, -1, -1)
