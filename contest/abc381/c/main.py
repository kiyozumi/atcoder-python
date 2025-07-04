import re


N = int(input())
S = input()

ans = 1
pattern = r"1+/2+"
matches = re.findall(pattern, S)
if matches:
    for m in matches:
        ones, twos = m.split("/")
        length = min(len(ones), len(twos)) * 2 + 1
        if ans < length:
            ans = length
print(ans)
