S = input()

uppercase_count = sum(1 for c in S if c.isupper())
if len(S) - uppercase_count < uppercase_count:
    print(S.upper())
else:
    print(S.lower())
