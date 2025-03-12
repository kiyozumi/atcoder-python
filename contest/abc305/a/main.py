N = int(input())

r = N % 10
if r < 3:
    print(N - r)
else:
    print(N + 5 - r)
