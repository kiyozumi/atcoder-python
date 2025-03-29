N = int(input())
S = [input() for _ in range(N)]

result = {i + 1: s.count("o") for i, s in enumerate(S)}
ans = sorted(result, key=result.get, reverse=True)
print(*ans)
