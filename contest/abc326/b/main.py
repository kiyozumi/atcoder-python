N = int(input())

for n in range(N, 919 + 1):
    h, t, o = [int(x) for x in list(str(n))]
    if h * t == o:
        print(n)
        exit()
