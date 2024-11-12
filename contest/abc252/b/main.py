N, K = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]

max = max(A)
for b in B:
    if A[b - 1] == max:
        print("Yes")
        exit()

print("No")
