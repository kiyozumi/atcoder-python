LR = input().replace(" ", "")

match (LR):
    case "10":
        print("Yes")
    case "01":
        print("No")
    case _:
        print("Invalid")
