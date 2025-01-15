T = int(input())

for _ in range(T):
    N = int(input())
    A = [int(x) for x in input().split()]
    ans = [x for x in A if x % 2 != 0]
    print(len(ans))
