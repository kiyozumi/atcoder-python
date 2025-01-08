import re

S = input()

# 100000 以上 999999 以下
if re.match(r"^[A-Z][1-9][0-9]{5}[A-Z]$", S):
    print("Yes")
else:
    print("No")
