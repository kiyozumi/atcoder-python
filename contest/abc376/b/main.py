def move_position(n: int, from_: int, to_: int, ng: int):
    if from_ > to_:
        from_, to_ = to_, from_
    if from_ < ng < to_:
        return N + from_ - to_
    else:
        return to_ - from_


N, Q = [int(x) for x in input().split()]

l = 1
r = 2
ans = 0
for _ in range(Q):
    H, T = input().split()
    T = int(T)
    match H:
        case "L":
            ans += move_position(N, l, T, r)
            l = T
        case "R":
            ans += move_position(N, r, T, l)
            r = T
print(ans)
