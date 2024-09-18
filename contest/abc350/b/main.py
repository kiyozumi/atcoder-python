N, Q = [int(x) for x in input().split()]
T = [int(x) for x in input().split()]
teeth = [1] * N

for t in T:
    teeth[t - 1] ^= 1

print(teeth.count(1))

# N, Q = [int(x) for x in input().split()]
# T = [int(x) for x in input().split()]
#
# teeth = ["*"] * N
# for t in T:
#     if teeth[t - 1] == "*":
#         teeth[t - 1] = ""
#     else:
#         teeth[t - 1] = "*"
#
# print(teeth.count("*"))
