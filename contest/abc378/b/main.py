N = int(input())
schedules = [[int(x) for x in input().split()] for _ in range(N)]
Q = int(input())
for _ in range(Q):
    t, d = [int(x) for x in input().split()]
    q, r = schedules[t - 1]
    ans = d + ((r - d) % q)
    print(ans)
