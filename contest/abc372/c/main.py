N, Q = [int(x) for x in input().split()]
S = input()
count = S.count("ABC")
S = list(S)

for _ in range(Q):
    X, C = input().split()
    X = int(X) - 1
    before = "".join(S[max(0, X - 2) : min(X + 3, N + 1)]).count("ABC")
    S[X] = C
    after = "".join(S[max(0, X - 2) : min(X + 3, N + 1)]).count("ABC")
    count += after - before
    print(count)
