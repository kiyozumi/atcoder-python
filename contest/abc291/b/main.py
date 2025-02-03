N = int(input())
X = sorted([int(x) for x in input().split()])
A = X[N:-N]
print(sum(A) / len(A))
