from sortedcontainers import SortedList

cheeses = SortedList()
N, W = [int(x) for x in input().split()]
for _ in range(N):
    A, B = [int(x) for x in input().split()]
    cheeses.add([A, B])

ans = 0
g = W
for a, b in reversed(cheeses):
    if g < b:
        b = g

    ans += a * b
    g -= b
    if g == 0:
        break
print(ans)
