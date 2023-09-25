A, B, C, X = [int(x) for x in open(0)]

total = 0
for i in range(A + 1):
    for j in range(B + 1):
        for k in range(C + 1):
            if i * 500 + j * 100 + k * 50 == X:
                total += 1
print(total)
