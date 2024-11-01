S = [int(x) for x in input()]

for i in range(10):
    if i not in S:
        print(i)
        exit()
