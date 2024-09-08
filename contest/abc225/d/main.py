N, Q = [int(x) for x in input().split()]
front = [0] * (N + 1)
back = [0] * (N + 1)

for _ in range(Q):
    q = [int(x) for x in input().split()]
    match q[0]:
        case 1:
            x, y = q[1], q[2]
            front[x] = y
            back[y] = x
        case 2:
            x, y = q[1], q[2]
            front[x] = 0
            back[y] = 0
        case 3:
            x = q[1]
            ans = []
            f = []
            f.append(x)
            train = front[x]
            while train != 0:
                f.append(train)
                train = front[train]
            b = []
            train = back[x]
            while train != 0:
                b.append(train)
                train = back[train]
            ans = b[::-1] + f
            print(len(ans), *ans)
