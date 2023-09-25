N = int(input())

prev_t, prev_x, prev_y = 0, 0, 0

for _ in range(N):
    t, x, y = [int(x) for x in input().split()]
    dist_count = abs(x - prev_x) + abs(y - prev_y)
    time_diff = t - prev_t
    if dist_count > time_diff or (time_diff - dist_count) % 2 != 0:
        print("No")
        exit()

    prev_t, prev_x, prev_y = t, x, y

print("Yes")
