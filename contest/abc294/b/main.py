from string import ascii_uppercase

table = "." + ascii_uppercase

H, W = [int(x) for x in input().split()]
for _ in range(H):
    A = [int(x) for x in input().split()]
    ans = ""
    for a in A:
        ans += table[a]
    print(ans)
