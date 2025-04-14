N = int(input())
A = [input() for _ in range(N)]
B = [input() for _ in range(N)]


for i, (a, b) in enumerate(zip(A, B)):
    if a == b:
        continue

    for j in range(N):
        if a[j] != b[j]:
            print(i + 1, j + 1)
            exit()
