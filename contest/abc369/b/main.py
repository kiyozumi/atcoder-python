N = int(input())

ans = 0
l, r = 0, 0
for i in range(N):
    A, S = input().split()
    A = int(A)
    match S:
        case "L":
            if l != 0:
                ans += abs(A - l)
            l = A
        case "R":
            if r != 0:
                ans += abs(A - r)
            r = A
print(ans)
