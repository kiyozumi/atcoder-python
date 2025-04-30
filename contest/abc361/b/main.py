def is_overlapped(t1: tuple[int, int], t2: tuple[int, int]) -> bool:
    if max(t1) < min(t2):
        return True
    else:
        return False


a, b, c, d, e, f = [int(x) for x in input().split()]
g, h, i, j, k, l = [int(x) for x in input().split()]

if (
    is_overlapped((a, g), (d, j))
    and is_overlapped((b, h), (e, k))
    and is_overlapped((c, i), (f, l))
):
    print("Yes")
else:
    print("No")
