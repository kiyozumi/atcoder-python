M = int(input())
D = [int(x) for x in input().split()]

mid = (sum(D) + 1) // 2
total = 0
for i, d in enumerate(D):
    total += d
    if total >= mid:
        print(i + 1, mid - (total - d))
        exit()
