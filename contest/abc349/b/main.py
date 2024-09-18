S = list(input())

d = {}
for c in S:
    d[c] = d.get(c, 0) + 1

v = list(d.values())
for n in range(1, len(S) + 1):
    if v.count(n) != 0 and v.count(n) != 2:
        print("No")
        exit()

print("Yes")
