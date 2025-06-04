S = input()
T = input()

if S == T:
    print(0)
else:
    n = min(len(S), len(T))
    if S[:n] == T[:n]:
        print(n + 1)
    else:
        for i, (s, t) in enumerate(zip(S, T)):
            if s != t:
                print(i + 1)
                break
