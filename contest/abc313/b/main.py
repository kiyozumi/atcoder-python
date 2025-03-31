N, M = [int(x) for x in input().split()]
losers = set(int(input().split()[1]) for _ in range(M))

players = set(range(1, N + 1))

ans = players - losers
print(*ans) if len(ans) == 1 else print(-1)
