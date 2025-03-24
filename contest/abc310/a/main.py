N, P, Q = [int(x) for x in input().split()]
D = [int(x) for x in input().split()]

print(P) if P < Q + min(D) else print(Q + min(D))
