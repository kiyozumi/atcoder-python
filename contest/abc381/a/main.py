N = int(input())
S = input()

if N % 2 == 0:
    print("No")
    exit()

if N == 1 and S == "/":
    print("Yes")
    exit()

if (
    "1" not in S[: (N + 1) // 2 - 1]
    or "/" != S[(N + 1) // 2 - 1]
    or "2" not in S[(N + 1) // 2 - 1 :]
):
    print("No")
else:
    print("Yes")
