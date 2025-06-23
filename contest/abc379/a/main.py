N = input()

ans1 = N[1:] + N[0]
ans2 = N[-1] + N[:2]
print(ans1, ans2)
