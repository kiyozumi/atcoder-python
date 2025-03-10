N = int(input())
S, A = [], []
for _ in range(N):
    s, a = input().split()
    S.append(s)
    A.append(int(a))

min_idx = A.index(min(A))
for s in S[min_idx:] + S[0:min_idx]:
    print(s)
