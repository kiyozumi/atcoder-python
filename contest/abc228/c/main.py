N, K = [int(x) for x in input().split()]
scores = []
for _ in range(N):
    P = [int(x) for x in input().split()]
    scores.append(sum(P))

limit = sorted(scores, reverse=True)[K - 1]
for s in scores:
    if (s + 300) >= limit:
        print("Yes")
    else:
        print("No")
