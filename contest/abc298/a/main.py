# o は「良」、- は「可」、x は 「不可」
N = int(input())
S = input()

if S.count("o") >= 1 and S.count("x") == 0:
    print("Yes")
else:
    print("No")
