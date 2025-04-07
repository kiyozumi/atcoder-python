N = int(input())
A = [int(x) for x in input().split()]
sorted_A = sorted(A)

for i in range(len(A) - 1):
    if sorted_A[i + 1] - sorted_A[i] != 1:
        print(sorted_A[i] + 1)
        exit()
