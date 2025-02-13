from string import ascii_lowercase

S = open(0).read().split()
for i, s in enumerate(reversed(S), 1):
    if "*" in s:
        column = ascii_lowercase[s.index("*")]
        print(f"{column}{i}")
