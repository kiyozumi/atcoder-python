S = input()

d = {}
upper_flg = False
lower_flg = False
for s in S:
    if s.isupper():
        upper_flg = True
    if s.islower():
        lower_flg = True
    if d.get(s, False):
        print("No")
        exit()
    d[s] = True

if upper_flg and lower_flg and lower_flg:
    print("Yes")
else:
    print("No")
