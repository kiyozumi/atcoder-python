from itertools import combinations_with_replacement

# 4ab+3a+3b
N = int(input())
S = [int(x) for x in input().split()]

areas = {}
for a, b in combinations_with_replacement(range(1, 1001), 2):
    area = (4 * a * b) + (3 * a) + (3 * b)
    areas[area] = True

ans = 0
for s in S:
    if not areas.get(s, False):
        ans += 1

print(ans)
