H = int(input())

h = 0
day = 0
while h <= H:
    h += 1 << day
    day += 1
print(day)
