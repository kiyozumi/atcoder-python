from itertools import permutations

N, *A = open(0).read().split()
target = list(permutations(range(int(N)), 2))
contradiction = False
for i, j in target:
    match A[i][j]:
        case "W":
            if A[j][i] != "L":
                print("incorrect")
                exit()
        case "L":
            if A[j][i] != "W":
                print("incorrect")
                exit()
        case "D":
            if A[j][i] != "D":
                print("incorrect")
                exit()
print("correct")
