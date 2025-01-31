N, K = [int(x) for x in input().split()]
S = input()
k = 0

for i in range(N):
    if S[i] == "o":
        k += 1
        if k == K:
            print(S[: i + 1] + "x" * (N - i - 1))
            exit()
