S = list(input())
d = {}
for s in S:
    d[s] = d.get(s, 0) + 1

for k, v in d.items():
    if v == 1:
        print(k)
        exit()
print(-1)
