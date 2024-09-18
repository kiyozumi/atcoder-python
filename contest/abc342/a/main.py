S = input()

d = {}
for i, s in enumerate(S):
    d[s] = d.get(s, 0) + 1

for k, v in d.items():
    if v == 1:
        l, r = S.split(k)
        print(len(l) + 1)
        exit()
