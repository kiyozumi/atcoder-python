Q = int(input())

d = {}
for _ in range(Q):
    q = input().split()
    match q[0]:
        case "1":
            d[q[1]] = d.get(q[1], 0) + 1
        case "2":
            if q[1] in d:
                d[q[1]] -= 1
                if d[q[1]] <= 0:
                    del d[q[1]]
        case "3":
            print(len(d.keys()))
