N = int(input())
S = input().translate(str.maketrans("10", "lo"))
T = input().translate(str.maketrans("10", "lo"))

print("Yes" if S == T else "No") if S == T else print("No")
