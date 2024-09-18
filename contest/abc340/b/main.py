Q = int(input())
A = []
for _ in range(Q):
    t, x = [int(x) for x in input().split()]
    match t:
        case 1:
            A.append(x)
        case 2:
            print(A[-x])
