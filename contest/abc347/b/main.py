S = input()
N = len(S)
ans = set()

for i in range(1, N + 1):
    j = 0
    while i + j <= N:
        # print(f"{S[j:j+i]} i={i} j={j} [{j}:{j+i}]")
        ans.add(S[j : j + i])
        j += 1

print(len(ans))
