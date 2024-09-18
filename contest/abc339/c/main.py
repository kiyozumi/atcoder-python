N = int(input())
A = [int(x) for x in input().split()]

m = 0
sum = 0
for a in A:
    sum += a
    m = min(m, sum)
print(sum - m)
