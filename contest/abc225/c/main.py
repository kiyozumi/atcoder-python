N, M = [int(x) for x in input().split()]
B = [[int(x) for x in input().split()] for _ in range(N)]
base_column = B[0][0] % 7
if base_column == 0 and M > 1:
    print("No")
    exit()
if 8 < base_column + M:
    print("No")
    exit()

base_row = B[0][0]
for b in B:
    if base_row != b[0]:
        print("No")
        exit()
    for j in range(M):
        if b[j] != base_row + j:
            print("No")
            exit()
    base_row += 7

print("Yes")
