A, B, C, X = [int(x) for x in input().split()]

if X <= A:
    print(1.0)
    exit()

if X > B:
    print(0.0)
    exit()

print(C / (B - A))
