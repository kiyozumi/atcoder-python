N = int(input())
A = [int(x) for x in input().split()]
Q = int(input())

for _ in range(Q):
    q = [int(x) for x in input().split()]
    match (q[0]):
        case 1:
            k, x = q[1:]
            A[k - 1] = x
        case 2:
            k = q[1]
            print(A[k - 1])
