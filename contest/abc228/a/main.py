S, T, X = [int(x) for x in input().split()]
if T < S:
    T += 24
if X < S:
    X += 24

if S <= X < T:
    print("Yes")
else:
    print("No")
