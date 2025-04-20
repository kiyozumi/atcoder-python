N, M = [int(x) for x in input().split()]
S = input()
T = input()

prefix = T[:N]
suffix = T[-N:]
if S == prefix and S == suffix:
    print(0)
elif S == prefix and S != suffix:
    print(1)
elif S != prefix and S == suffix:
    print(2)
else:
    print(3)
