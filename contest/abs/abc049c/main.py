S = input().strip()[::-1]

words = [word[::-1] for word in ["dream", "dreamer", "erase", "eraser"]]

while len(S) > 0:
    matched = False
    for word in words:
        if S.startswith(word):
            S = S[len(word) :]
            matched = True
            break
    if not matched:
        break

print("YES" if len(S) == 0 else "NO")
