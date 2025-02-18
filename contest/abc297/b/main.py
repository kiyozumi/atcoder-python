import re


S = input()

left = S.find("B") % 2
right = S.rfind("B") % 2
if left == right:
    print("No")
    exit()

if re.match(r"^.*R.*K.*R.*$", S):
    print("Yes")
else:
    print("No")
