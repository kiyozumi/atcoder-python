N = int(input())
A = [int(x) for x in input().split()]
X = int(input())

quotient, remainder = divmod(X, sum(A))

ans = quotient * N
sum = 0
for a in A:
    sum += a
    ans += 1
    if sum > remainder:
        break

print(ans)
