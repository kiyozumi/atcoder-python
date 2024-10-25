from numpy import number

N = int(input())
numbers = {}
for i in range(1, (2 * N + 1) + 1):
    numbers[i] = i

for _ in range(N + 1):
    k, v = numbers.popitem()
    print(k)

    n = int(input())
    if n == 0:
        break
    numbers.pop(n)
