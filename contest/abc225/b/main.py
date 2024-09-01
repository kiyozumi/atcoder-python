N = int(input())
counter = {}
for _ in range(N - 1):
    a, b = [int(x) for x in input().split()]
    counter[a] = counter.get(a, 0) + 1
    counter[b] = counter.get(b, 0) + 1

for x in counter.values():
    if x == (N - 1):
        print("Yes")
        exit()
print("No")
