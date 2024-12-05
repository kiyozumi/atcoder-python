S = open(0).read().split()

row = ""
A, B = 10, 0
for i, s in enumerate(S, 1):
    if "#" in s:
        A = min(A, i)
        B = max(B, i)
        row = s

C = row.find("#") + 1
D = row.rfind("#") + 1
print(A, B)
print(C, D)
