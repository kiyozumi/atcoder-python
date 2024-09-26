import re

N = int(input())
result = re.search(r"0*$", format(N, "b"))
print(len(result.group()))
