# 自分で作った解答
# N = int(input())
# P = [int(x) for x in input().split()]
#
# print(max(0, max(P[1:]) - P[0] + 1))

# 解答例
N = int(input())
P = list(map(int, input().split()))
ma = max(P)
if P[0] == ma and ma not in P[1:]:
    print(0)
else:
    if len(P) == 1:
        print(0)
    else:
        print(ma - P[0] + 1)
