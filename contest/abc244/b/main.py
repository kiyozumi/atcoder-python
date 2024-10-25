N = int(input())
T = input()

x, y = 0, 0
next_direction = {"E": "S", "S": "W", "W": "N", "N": "E"}
direction = "E"

for t in T:
    match (t):
        case "S":
            match (direction):
                case "E":
                    x += 1
                case "S":
                    y -= 1
                case "W":
                    x -= 1
                case "N":
                    y += 1
        case "R":
            direction = next_direction[direction]

print(x, y)
