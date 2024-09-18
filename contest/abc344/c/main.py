N = int(input())
A = [int(x) for x in input().split()]
M = int(input())
B = [int(x) for x in input().split()]
L = int(input())
C = [int(x) for x in input().split()]
Q = int(input())
X = [int(x) for x in input().split()]

sum_set = set()
for a in A:
    for b in B:
        for c in C:
            sum_set.add(a + b + c)
for x in X:
    if x in sum_set:
        print("Yes")
    else:
        print("No")
