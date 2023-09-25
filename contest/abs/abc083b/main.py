N, A, B = [int(x) for x in input().split()]

total = 0
for i in range(1, N + 1):
    n = sum([int(x) for x in str(i)])
    if A <= n <= B:
        total += i

print(total)
