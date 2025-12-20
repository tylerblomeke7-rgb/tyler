# shoppingList = ["milk", "eggs", "bread"]

# print("shopping list:",shoppingList)
# for i in range(len(shoppingList)):
#     print("shopping list at index", i, shoppingList[i])

# shoppingDict = {"dairy": "milk", "protein": "eggs", "grain": "bread"}
# print("shopping dictionary:",shoppingDict)
# for i in shoppingDict:
#      print("shopping dictionary at index", i, shoppingDict[i])

world = {
    1: {"up": 2, "down": 16, "right": 14},
    2: {"up": 3, "down": 1, "right": 15, "left": 5},
    3: {"down": 2,"left": 4},
    4: {"down": 6, "right": 3},
    5: { "down":7, "right":2 },
    6: {"up": 4,  "right":7},
    7: {"up":5, "down": 8, "right": 16, "left": 6},
    8: {"up": 7,  "right": 9},
    9: { "down":11 , "right": 10, "left": 8},
    10: {"up":14,  "left": 9},
    11: {"up":9,  "right": 12 },
    12: {"up": 13,  "left": 11},
    13: { "down": 12, "left": 14},
    14: {"up":15, "down":10, "right": 13, "left": 1},
    15: { "down": 14, "left": 2},
    16: {"up": 1,  "left": 7},
}

location = 1

while True:
    print(f"You are at location {location}")
    userInput = input("Move (up, down, left, right or quit): ").lower()

    if userInput == "quit":
        break

    if userInput in world[location]:
        location = world[location][userInput]
    else:
        print("You are at a Wall")
