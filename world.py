# shoppingList = ["milk", "eggs", "bread"]

# print("shopping list:",shoppingList)
# for i in range(len(shoppingList)):
#     print("shopping list at index", i, shoppingList[i])

# shoppingDict = {"dairy": "milk", "protein": "eggs", "grain": "bread"}
# print("shopping dictionary:",shoppingDict)
# for i in shoppingDict:
#      print("shopping dictionary at index", i, shoppingDict[i])
import random

location = 1
cart = []
totalSum = 0
playerMoney = random.randint(10, 100)
chance = random.randint(1, 1000000)
value = 32
API_Key = "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"
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

locationNames = {
    1: "entrance",
    2: "produce",
    3: "dairy",
    4: "hallway",
    5: "grains",
    6: "meat",
    7: "beverages",
    8: "candy",
    9: "hallway",
    10: "restaurant",
    11: "pharmacy",
    12: "hallway",
    13: "clothing",
    14: "helpdesk",
    15: "checkout",
    16: "exit", 
}


store = {
    "produce": {
        "apples": 3,
        "bananas": 5,
        "carrots": 4,
        "lettuce": 2
    },

    "dairy": {
        "milk": 4,
        "cheese": 6,
        "yogurt": 5,
        "butter": 3
    },

    "grains": {
        "bread": 3,
        "rice": 10,
        "pasta": 4,
        "cereal": 5
    },

    "meat": {
        "chicken": 8,
        "beef": 12,
        "pork": 9,
        "fish": 11
    },

    "beverages": {
        "water": 2,
        "soda": 3,
        "juice": 4,
        "coffee": 6
    },

    "candy": {
        "chocolate": 2,
        "gummies": 1,
        "lollipop": 1,
        "caramel": 2
    },

    "restaurant": {
        "burger": 10,
        "pizza": 12,
        "salad": 8,
        "fries": 4
    },

    "pharmacy": {
        "pain_reliever": 6,
        "vitamins": 10,
        "bandages": 4,
        "cough_syrup": 7
    },

    "clothing": {
        "t_shirt": 15,
        "jeans": 40,
        "jacket": 60,
        "socks": 5
    }
}

# Returns the name of a location based on its location number
# Takes locationNumber as input and searches the locationNames dictionary
# Returns the location name if found, otherwise returns "Not a Location"
def returnLocationName (locationNumber):
    if locationNumber in locationNames:
        return locationNames[locationNumber]
    else:
        return "Not a Location"
    
# Displays all available exits from the current location
# Retrieves the available directions (up, down, left, right) from the world dictionary
# Prints each direction and the corresponding destination location name in a formatted list
def movementNames(location):
    print("\n" + "-" * 60)
    print("  AVAILABLE EXITS:")
    print("-" * 60)
    for i in world[location]:
        print(f"    ➜  Move {i.upper():<8} to {returnLocationName(world[location][i]).upper()}")
    print("-" * 60)
        
# Displays all products available at the current location
# Checks if the location name exists in the store dictionary
# If products are available, prints each item with a numbered list and its price in a formatted table
# If no products are available, displays an informational message
def displayProducts(location):
    location_name = returnLocationName(location)
    if location_name in store:
        print("\n" + "=" * 60)
        print(f"  🛒 PRODUCTS AVAILABLE AT {location_name.upper()}:")
        print("=" * 60)
        item_number = 1
        for item, price in store[location_name].items():
            print(f"    {item_number}. {item.replace('_', ' ').title():<23} ${price:>5}")
            item_number += 1
        print("=" * 60)
    else:
        print("\n    ℹ️  No products available here.\n")

# Displays the current shopping cart and calculates the total price
# Iterates through all items in the cart and searches the store dictionary to find prices
# Prints each cart item with its price and displays the total sum at the bottom
# Updates the global totalSum variable with the calculated price
def displayCart():
    global totalSum
    
    totalPrice = 0
    
    print("\n" + "=" * 60)
    print("  🛍️  YOUR SHOPPING CART:")
    print("=" * 60)
    
    if not cart:
        print("    (Cart is empty)")
    else:
        for i in cart:
            for j in store:
                for k in store[j]:
                    if k == i:     
                        print(f"    • {i.replace('_', ' ').title():<25} ${store[j][k]:>5}")
                        totalPrice = totalPrice + store[j][k]
        print("-" * 60)
        print(f"    TOTAL PRICE: ${totalPrice:>5}")
    
    print("=" * 60)
    
    totalSum = totalPrice

# Allows the player to browse and add items to their cart at product locations
# Only runs if the current location is in the product_locations_list (stores with items)
# Displays available products with numbered items and repeatedly prompts the player to enter item numbers
# Converts the location to a store category and maps item numbers to actual product names
# Continues looping until the player enters 'x' to stop shopping
# Displays the updated cart after each item is added with error handling for invalid numbers
def buyProducts(location):
    product_locations_list = [2, 3, 5, 6, 7, 8, 10, 11, 13]
    
    if location in product_locations_list:
        location_name = returnLocationName(location)
        displayProducts(location)
        
        # Create a list of items for this location to map numbers to product names
        items_list = list(store[location_name].keys())
        
        userInput = input("\n  ➤ Enter item number to add to cart (or 'x' to stop): ").lower()
    
        while userInput != 'x':
            try:
                item_index = int(userInput) - 1
                if 0 <= item_index < len(items_list):
                    item_name = items_list[item_index]
                    cart.append(item_name)
                    print(f"\n    ✓ Added '{item_name.replace('_', ' ').title()}' to cart!")
                    displayCart()
                else:
                    print(f"\n    ⚠️  Invalid item number! Please enter a number between 1 and {len(items_list)}.")
            except ValueError:
                print("\n    ⚠️  Please enter a valid number or 'x' to stop!")
            
            userInput = input("\n  ➤ Enter item number to add to cart (or 'x' to stop): ").lower()
        
        print(f"\n    👋 Thank you for visiting {returnLocationName(location).upper()}!\n")
    
def checkoutCart(location):
    global playerMoney, totalSum, cart
    if location == 15:
        while True:
            displayCart()
            print(f"You have ${playerMoney} in your wallet.")
            
            userInput = input("\nPress a to buy cart\nPress x to review/remove items: ").lower()
            
            if userInput == 'a':
                if not cart:
                    print("\n    ℹ️  Your cart is empty!")
                    break
                # Check if player has enough money
                if playerMoney >= totalSum:
                    playerMoney = playerMoney - totalSum
                    cart = []  # Clear cart after purchase
                    print(f"\n    ✓ Purchase successful! You have ${playerMoney} left")
                    break
                else:
                    print(f"\n    ⚠️  Insufficient funds! You need ${totalSum - playerMoney} more.")
                    
            elif userInput == 'x':
                # Review and remove items from cart
                if not cart:
                    print("\n    ℹ️  Your cart is empty!")
                    break
                else:
                    print("\n" + "=" * 60)
                    print("  🛍️  ITEMS IN YOUR CART:")
                    print("=" * 60)
                    for idx, item in enumerate(cart):
                        print(f"    {idx + 1}. {item.replace('_', ' ').title()}")
                    print("=" * 60)
                    
                    removeInput = input("\n  ➤ Enter item number to remove (or 'x' to continue): ").lower()
                    while removeInput != 'x':
                        try:
                            itemIndex = int(removeInput) - 1
                            if 0 <= itemIndex < len(cart):
                                removed_item = cart.pop(itemIndex)
                                print(f"\n    ✓ Removed '{removed_item.replace('_', ' ').title()}' from cart!")
                                # Recalculate total
                                displayCart()
                            else:
                                print("\n    ⚠️  Invalid item number!")
                        except ValueError:
                            print("\n    ⚠️  Please enter a valid number!")

                        removeInput = input("\n  ➤ Enter item number to remove (or 'x' to continue): ").lower()
            else:
                print("\n    ⚠️  Invalid input! Please press 'a' or 'x'.")

def robbing(location):
    global chance, value, playerMoney, cart, totalSum
    if location == 12:
        if chance == value:
            print("\n    💰 You successfully robbed the store and got $100! Congratulations!")
            playerMoney += 100
            cart = []
            totalSum = 0
        else:
            print("\n    🚨 You got caught trying to rob the store! Game over.")
            print(f"    💸 You lost all your money and items. You had ${playerMoney} and {len(cart)} items in your cart.")
            playerMoney = 0
            cart = []
            totalSum = 0   

import requests
import json
def GPT(personality, role, location):
    persona = f"You are {personality}"
    instruction = f"You are a {role}. Say a sentence as that role."
    context = f"You are at location:{location} inside a grocery store. the customer you are talking to has {cart} items in their cart."
    format = "Only the content the character is saying. No explanations"
    audience = "The customer that the charcater is talking to."
    tone = f"You have the tone of this personality {personality}"
    data = f"movement across the grocery store = {world}. Aisle names = {locationNames}. products sorted by aisle and category = {store}."
    response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {API_Key}",
        "Content-Type": "application/json",
        "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
        "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
    },
    data=json.dumps({
        "model": "liquid/lfm-2.5-1.2b-instruct:free",
        "messages": [
        {
            "role": "user",
            "content": f"persona = {persona}. intruction = {instruction}. context = {context}. format = {format}. audience = {audience}. tone = {tone}. data = {data}"
        }
        ]
    })
    )

    
    print(f"{response.json()["choices"][0]["message"]["content"]}")

def differentCharacters(location):
    if location == 1:
        GPT("extremely angry at his wife for making him shop by himself","customer",location)
    elif location == 2:
        GPT("Risk-taking behavior", "customer", location)
    elif location == 3:
        GPT("Relaxed, easy-going, patient", "customer", location)
    elif location == 4:
        GPT("Competitive, ambitious, impatient", "customer", location)
    elif location == 5:
        GPT("How they treat others", "customer", location)
    elif location == 6:
        GPT("Energetic, creative, people-oriented", "customer", location)
    elif location == 7:
        GPT("Social energy levels ", "employee", location)
    elif location == 8:
        GPT("Emotional intelligence", "customer", location)
    elif location == 9:
        GPT("Neuroticism  Sensitive vs Emotionally Stable", "customer", location)
    elif location == 10:
        GPT("Stability and security", "customer", location)
    elif location == 11:
        GPT("How they react to criticism", "employee", location)
    elif location == 12:
        GPT("Optimistic or pessimistic", "employee", location)
    elif location == 13:
        GPT("Power and influence", "employee", location)
    elif location == 14:
        GPT("taiking to manager", "manager", location)
    elif location == 15:
        GPT("talking to a cashier", "cashier", location)

import random
import sys

# ...existing code...

# Main game loop that handles player movement and interaction
# Displays the current location name and calls buyProducts and checkoutCart functions
# Shows available exits and prompts the player to enter physical arrow keys to move
# Captures raw keyboard input without requiring Enter key press
# Maps physical arrow keys to directions (up, down, left, right)
# Updates the global location variable if a valid arrow key is entered
# Displays an error message if the player tries to move in an invalid direction
def movement():
    global location
    
    print("\n" + "=" * 60)
    print(f"  📍 CURRENT LOCATION: {returnLocationName(location).upper()}")
    print("=" * 60)
    
    buyProducts(location)
    movementNames(location)
    checkoutCart(location)
    robbing(location)
    differentCharacters(location)

    
    
    print("\n  ➤ Press arrow key to move (UP/DOWN/LEFT/RIGHT):")
    
    # Capture raw keyboard input
    if sys.platform == "win32":
        import msvcrt
        key = msvcrt.getch()
        
        # Map Windows arrow key codes to directions
        if key == b'\xe0':  # Special key indicator for Windows
            arrow_key = msvcrt.getch()
            arrow_map = {
                b'H': 'up',      # Up arrow
                b'P': 'down',    # Down arrow
                b'K': 'left',    # Left arrow
                b'M': 'right'    # Right arrow
            }
            
            if arrow_key in arrow_map:
                direction = arrow_map[arrow_key]
                if direction in world[location]:
                    location = world[location][direction]
                else:
                    print("\n    ⚠️  You are at a wall! Please choose a valid direction.\n")
            else:
                print("\n    ⚠️  Invalid input! Please press an arrow key.\n")
        else:
            print("\n    ⚠️  Invalid input! Please press an arrow key.\n")
    else:
        # For non-Windows systems (Linux/Mac)
        print("    (Arrow key support requires Windows. Use ↑/↓/←/→ symbols instead)")

while True:
    movement()