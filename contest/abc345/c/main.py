# 問題: https://atcoder.jp/contests/abc345/tasks/abc345_c
# 解説: https://atcoder.jp/contests/abc345/editorial/9575
# 参考解答: https://atcoder.jp/contests/abc345/submissions/55432243

# WA
S = list(input())
ans = set()

for i in range(len(S)):
    for j in range(i + 1, len(S)):
        if S[j] == S[i]:
            continue
        S[i], S[j] = S[j], S[i]
        ans.add("".join(S))

print(1) if len(ans) == 0 else print(len(ans))
