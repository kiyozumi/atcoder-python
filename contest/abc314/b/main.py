N = int(input())
players = [[] for _ in range(N)]

for i in range(N):
    C = int(input())
    A = [int(x) for x in input().split()]
    players[i] = A

X = int(input())
winners = {i + 1: p for i, p in enumerate(players) if X in p}
if len(winners) == 0:
    print(0)
    exit()

ans = []
m = min(len(v) for v in winners.values())
for k, v in winners.items():
    if len(v) == m:
        ans.append(k)

print(len(ans))
print(*ans)
