s = input()

ans = s.translate(str.maketrans("01", "10"))
print(ans)
