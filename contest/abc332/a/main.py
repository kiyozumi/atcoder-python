(N, S, K), *I = [[int(x) for x in s.split()] for s in open(0)]

total = 0
for P, Q in I:
    total += P * Q

if total < S:
    total += K
print(total)
