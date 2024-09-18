def is_palindromic_number(x: int) -> bool:
    k = str(x)
    if k == k[::-1]:
        return True
    else:
        return False


N = int(input())
ans = 0
i = 1
while i**3 <= N:
    if is_palindromic_number(i**3):
        ans = i**3
    i += 1
print(ans)
