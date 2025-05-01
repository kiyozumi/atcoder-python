xa, ya = [int(x) for x in input().split()]
xb, yb = [int(x) for x in input().split()]
xc, yc = [int(x) for x in input().split()]

ab = (xa - xb) ** 2 + (ya - yb) ** 2
bc = (xb - xc) ** 2 + (yb - yc) ** 2
ca = (xc - xa) ** 2 + (yc - ya) ** 2

if ab + bc == ca or bc + ca == ab or ca + ab == bc:
    print("Yes")
else:
    print("No")
