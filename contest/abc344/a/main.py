S = input()

left, middle, right = S.split("|")
print(left + right)

# left = S.find("|")
# right = S.rfind("|")
# print(S[:left] + S[right + 1 :])
