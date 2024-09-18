S = "wbwbwwbwbwbw"
W, B = [int(x) for x in input().split()]

for i in range(len(S)):
    w_count = 0
    b_count = 0
    for j in range(W + B):
        if S[(i + j) % len(S)] == "w":
            w_count += 1
        else:
            b_count += 1

    if W == w_count and B == b_count:
        print("Yes")
        exit()

print("No")
