S = input()
print(S.translate(str.maketrans("", "", "aeiou")))
