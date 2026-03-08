import tkinter as tk
from tkinter import messagebox
import random
import requests
import json
import os
import threading

# ================== API CONFIG ==================

API_KEY = "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"

# ================== GAME DATA ==================

location = 1
cart = []
playerMoney = random.randint(25, 100)
npc_dialogue_cache = {}

world = {
    1: {"up": 2, "down": 16, "right": 14},
    2: {"up": 3, "down": 1, "right": 15, "left": 5},
    3: {"down": 2,"left": 4},
    4: {"down": 6, "right": 3},
    5: {"down":7, "right":2},
    6: {"up": 4, "right":7},
    7: {"up":5, "down": 8, "right": 16, "left": 6},
    8: {"up": 7, "right": 9},
    9: {"down":11 , "right": 10, "left": 8},
    10: {"up":14, "left": 9},
    11: {"up":9, "right": 12},
    12: {"up": 13, "left": 11},
    13: {"down": 12, "left": 14},
    14: {"up":15, "down":10, "right": 13, "left": 1},
    15: {"down": 14, "left": 2},
    16: {"up": 1, "left": 7},
}

locationNames = {
    1: "Entrance",
    2: "Produce",
    3: "Dairy",
    4: "Hallway",
    5: "Grains",
    6: "Meat",
    7: "Beverages",
    8: "Candy",
    9: "Hallway",
    10: "Restaurant",
    11: "Pharmacy",
    12: "Hallway",
    13: "Clothing",
    14: "Helpdesk",
    15: "Checkout",
    16: "Exit",
}

store = {
    "Produce": {"apples": 3, "bananas": 5, "carrots": 4, "lettuce": 2},
    "Dairy": {"milk": 4, "cheese": 6, "yogurt": 5, "butter": 3},
    "Grains": {"bread": 3, "rice": 10, "pasta": 4, "cereal": 5},
    "Meat": {"chicken": 8, "beef": 12, "pork": 9, "fish": 11},
    "Beverages": {"water": 2, "soda": 3, "juice": 4, "coffee": 6},
    "Candy": {"chocolate": 2, "gummies": 1, "lollipop": 1, "caramel": 2},
    "Restaurant": {"burger": 10, "pizza": 12, "salad": 8, "fries": 4},
    "Pharmacy": {"pain_reliever": 6, "vitamins": 10, "bandages": 4, "cough_syrup": 7},
    "Clothing": {"t_shirt": 15, "jeans": 40, "jacket": 60, "socks": 5}
}

npc_roles = {
    1: ("angry customer", "Extremely angry at his wife for making him shop"),
    2: ("risk-taking customer", "Impulsive and reckless"),
    3: ("relaxed customer", "Calm and easy-going"),
    4: ("competitive shopper", "Ambitious and impatient"),
    5: ("friendly shopper", "Very kind to others"),
    6: ("energetic shopper", "Creative and loud"),
    7: ("employee", "Social and outgoing"),
    8: ("emotional shopper", "Very expressive"),
    9: ("anxious shopper", "Sensitive and worried"),
    10: ("security-focused shopper", "Values stability"),
    11: ("pharmacy employee", "Defensive to criticism"),
    12: ("optimistic employee", "Overly positive"),
    13: ("fashion manager", "Power-driven"),
    14: ("store manager", "Authoritative"),
    15: ("cashier", "Professional and polite"),
}

# ================== HELPER FUNCTIONS ==================

def get_location_name():
    return locationNames.get(location, "Unknown")

# ================== NPC SYSTEM ==================

def talk_to_npc():
    if location not in npc_roles:
        display_npc_dialogue("There is no one to talk to here.")
        return

    if location in npc_dialogue_cache:
        display_npc_dialogue(npc_dialogue_cache[location])
        return

    display_npc_dialogue("NPC is thinking...")

    thread = threading.Thread(target=generate_npc_thread)
    thread.daemon = True
    thread.start()

def generate_npc_thread():
    dialogue = generate_npc_dialogue()
    npc_dialogue_cache[location] = dialogue
    root.after(0, lambda: display_npc_dialogue(dialogue))

def generate_npc_dialogue():
    if not API_KEY:
        return "API key not set."

    role, personality = npc_roles[location]

    prompt = f"""
    You are a {role}.
    Personality: {personality}.
    You are inside a grocery store at {get_location_name()}.
    The customer has these items in their cart: {cart}.
    Speak one short sentence in character.
    """

    try:
        response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
            "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
        },
        data=json.dumps({
            "model": "liquid/lfm-2.5-1.2b-instruct:free",
            "messages": [{"role": "user", "content": prompt}]
        }),
        timeout=10
        )

        return response.json()["choices"][0]["message"]["content"]

    except:
        return "The NPC stares silently..."

def display_npc_dialogue(dialogue):
    npc_text.config(state="normal")
    npc_text.delete("1.0", tk.END)
    npc_text.insert(tk.END, dialogue)
    npc_text.config(state="disabled")

# ================== STORE SYSTEM ==================

def update_display():
    location_label.config(text=f"📍 {get_location_name()}")
    money_label.config(text=f"💵 ${playerMoney}")
    update_products()
    update_cart()

def update_products():
    for widget in product_frame.winfo_children():
        widget.destroy()

    loc = get_location_name()
    if loc in store:
        for item, price in store[loc].items():
            tk.Button(
                product_frame,
                text=f"{item} - ${price}",
                command=lambda i=item: add_to_cart(i)
            ).pack(fill="x")

def update_cart():
    for widget in cart_frame.winfo_children():
        widget.destroy()

    total = 0
    for item in cart:
        for category in store:
            if item in store[category]:
                price = store[category][item]
                total += price
                tk.Label(cart_frame, text=f"{item} - ${price}").pack()

    tk.Label(cart_frame, text=f"Total: ${total}").pack()

def add_to_cart(item):
    cart.append(item)
    update_display()

def move(direction):
    global location
    if direction in world[location]:
        location = world[location][direction]
        update_display()
    else:
        messagebox.showwarning("Wall", "You can't move that way!")

def checkout():
    global playerMoney, cart
    if get_location_name() != "Checkout":
        messagebox.showinfo("Checkout", "Go to Checkout first!")
        return

    total = 0
    for item in cart:
        for category in store:
            if item in store[category]:
                total += store[category][item]

    if total == 0:
        messagebox.showinfo("Checkout", "Cart is empty!")
        return

    if playerMoney >= total:
        playerMoney -= total
        cart.clear()
        messagebox.showinfo("Success", "Purchase successful!")
    else:
        messagebox.showerror("Error", "Not enough money!")

    update_display()

# ================== GUI ==================

root = tk.Tk()
root.title("AI Grocery Store Simulator")
root.geometry("700x750")

location_label = tk.Label(root, font=("Arial", 18))
location_label.pack(pady=5)

money_label = tk.Label(root, font=("Arial", 14))
money_label.pack(pady=5)

movement_frame = tk.Frame(root)
movement_frame.pack(pady=10)

tk.Button(movement_frame, text="⬆", command=lambda: move("up")).grid(row=0, column=1)
tk.Button(movement_frame, text="⬅", command=lambda: move("left")).grid(row=1, column=0)
tk.Button(movement_frame, text="➡", command=lambda: move("right")).grid(row=1, column=2)
tk.Button(movement_frame, text="⬇", command=lambda: move("down")).grid(row=2, column=1)

tk.Button(root, text="💬 Talk to NPC", command=talk_to_npc, bg="#4CAF50", fg="white").pack(pady=10)

tk.Label(root, text="Products").pack()
product_frame = tk.Frame(root)
product_frame.pack(pady=5)

tk.Label(root, text="Cart").pack()
cart_frame = tk.Frame(root)
cart_frame.pack(pady=5)

tk.Button(root, text="🧾 Checkout", command=checkout, bg="blue", fg="white").pack(pady=10)

tk.Label(root, text="NPC Dialogue").pack()
npc_text = tk.Text(root, height=4, wrap="word")
npc_text.pack(fill="x", padx=20, pady=10)
npc_text.config(state="disabled")

update_display()
root.mainloop()