N = int(input())
A = [input() for _ in range(N)]

for row in range(N):
    if row == 0:
        print(A[1][0] + A[row][0:-1])
    elif row == N - 1:
        print(A[row][1:] + A[N - 2][-1])
    else:
        print(A[row + 1][0] + A[row][1:-1] + A[row - 1][-1])
