N, Q = [int(x) for x in input().split()]
ans = [0] * N
for _ in range(Q):
    event, player = [int(x) for x in input().split()]
    match event:
        case 3:
            if ans[player - 1] >= 2:
                print("Yes")
            else:
                print("No")
        case _:
            ans[player - 1] += event
