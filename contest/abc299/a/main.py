N = int(input())
S = input()

target = S[S.find("|") + 1 : S.rfind("|")]
if "*" in target:
    print("in")
else:
    print("out")
