x1, y1 = [int(x) for x in input().split()]
x2, y2 = [int(x) for x in input().split()]
x3, y3 = [int(x) for x in input().split()]

ans_x = x1 ^ x2 ^ x3
ans_y = y1 ^ y2 ^ y3

print(ans_x, ans_y)
