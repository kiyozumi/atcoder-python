N = int(input())
S = input()

c = N // 2
t, a = 0, 0
for s in S:
    match s:
        case "T":
            t += 1
            if t >= c:
                print("T")
                exit()
        case "A":
            a += 1
            if a >= c:
                print("A")
                exit()
