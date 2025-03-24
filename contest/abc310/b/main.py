N, M = [int(x) for x in input().split()]
items = [[int(x) for x in input().split()] for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == j:
            continue

        P_i = items[i][0]
        P_j = items[j][0]
        F_i = items[i][2:]
        F_j = items[j][2:]
        if P_i >= P_j and set(F_i).issubset(set(F_j)):
            if set(F_i).issubset(set(F_j)):
                if len(F_i) < len(F_j) or P_i > P_j:
                    print("Yes")
                    exit()

print("No")

#
