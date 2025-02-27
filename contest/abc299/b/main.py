from collections import defaultdict


N, T = [int(x) for x in input().split()]
C = [int(x) for x in input().split()]
R = [int(x) for x in input().split()]

players = defaultdict(dict)
for i in range(N):
    color, score, player_no = C[i], R[i], i + 1
    players[color][player_no] = score

target_color = T if T in players and players[T] else C[0]
scores = players[target_color]
ans = max(scores, key=scores.get)
print(ans)
