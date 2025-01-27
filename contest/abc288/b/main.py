N, K = [int(x) for x in input().split()]
names = []
for _ in range(K):
    names.append(input())

for name in sorted(names):
    print(name)
