N = int(input())
W = input().split()

words = ["and", "not", "that", "the", "you"]
if set(words) & set(W):
    print("Yes")
else:
    print("No")
