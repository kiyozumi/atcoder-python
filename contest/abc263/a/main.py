from collections import Counter

cards = [int(x) for x in input().split()]
c = Counter(cards)

if len(c.items()) == 2 and c.most_common(1)[0][1] == 3:
    print("Yes")
else:
    print("No")
