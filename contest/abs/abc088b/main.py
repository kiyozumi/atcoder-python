N = int(input())
a = [int(x) for x in input().split()]

alice = 0
bob = 0
for i, n in enumerate(reversed(sorted(a))):
    if i % 2 == 0:
        alice += n
    else:
        bob += n

print(alice - bob)
