R, G, B = [int(x) for x in input().split()]
C = input()

match (C):
    case "Red":
        print(min(G, B))
    case "Green":
        print(min(R, B))
    case "Blue":
        print(min(R, G))
