N = int(input())
S = []
T = []

for i in range(N):
    s, t = input().split()
    S.append(s)
    T.append(int(t))

idx = sum(T) % N
print(sorted(S)[idx])
