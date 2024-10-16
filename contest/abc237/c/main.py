S = input()

right_a_count = 0
for s in S[::-1]:
    if s != "a":
        break
    right_a_count += 1


left_a_count = 0
for s in S:
    if s != "a":
        break
    left_a_count += 1

if left_a_count > right_a_count:
    print("No")
    exit()
else:
    S = "a" * (right_a_count - left_a_count) + S

if S == S[::-1]:
    print("Yes")
else:
    print("No")
