N, M = [int(x) for x in input().split()]
S = [input() for _ in range(N)]


def is_tak_code(S: list, x: int, y: int) -> bool:
    top_left = ["###.", "###.", "###.", "...."]
    bottom_right = ["....", ".###", ".###", ".###"]
    if [item[y : y + 4] for item in S[x : x + 4]] == top_left and [
        item[y + 5 : y + 9] for item in S[x + 5 : x + 9]
    ] == bottom_right:
        return True
    else:
        return False


for i in range(N - 8):
    for j in range(M - 8):
        if is_tak_code(S, i, j):
            print(i + 1, j + 1)
