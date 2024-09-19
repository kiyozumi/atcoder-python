A, B = input().split()
for i in range(1, min(len(A), len(B)) + 1):
    a, b = int(A[-i]), int(B[-i])
    if (a + b) > 9:
        print("Hard")
        exit()

print("Easy")
