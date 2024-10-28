N = int(input())
A = set([int(x) for x in input().split()])

for i in range(len(A) + 1):
    if i not in A:
        print(i)
        break
