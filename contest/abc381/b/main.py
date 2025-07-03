from itertools import groupby


S = input()

if len(S) % 2 != 0:
    print("No")
    exit()

groups = ["".join(group) for key, group in groupby(S)]
d = {}
for g in groups:
    if len(g) == 2:
        if d.get(g):
            print("No")
            exit()
        else:
            d[g] = True
    else:
        print("No")
        exit()
print("Yes")
