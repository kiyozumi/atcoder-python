N, T, A = [int(x) for x in input().split()]

rest = N - (T + A)
if rest < abs(T - A):
    print("Yes")
else:
    print("No")
