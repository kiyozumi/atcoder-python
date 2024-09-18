N, T = [int(x) for x in input().split()]
score = [0] * N
d = {}
d[0] = N

for _ in range(T):
    A, B = [int(x) for x in input().split()]
    A -= 1
    past_score = score[A]
    d[past_score] -= 1
    if d[past_score] == 0:
        del d[past_score]
    score[A] += B
    new_score = score[A]
    d[new_score] = d.get(new_score, 0) + 1

    print(len(d))
