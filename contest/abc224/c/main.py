N = int(input())
A = [[int(x) for x in input().split()] for _ in range(N)]


def is_triangle(point_1: list, point_2: list, point_3: list) -> bool:
    x = 0
    y = 1
    if (
        (point_2[x] - point_1[x]) * (point_3[y] - point_1[y])
        - (point_3[x] - point_1[x]) * (point_2[y] - point_1[y])
    ) != 0:
        return True
    else:
        return False

    return True


ans = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if is_triangle(A[i], A[j], A[k]):
                ans += 1

print(ans)
