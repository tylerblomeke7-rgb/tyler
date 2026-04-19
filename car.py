import random
import os
import time

# ─────────────────────────────────────────────
#  CAR CLASSES
# ─────────────────────────────────────────────

class Inventions:
    def __init__(self, inventor):
        self.inventor = inventor

class Vehicle(Inventions):
    def __init__(self, inventor, topspeed, steering, lights, navigation, engine):
        super().__init__(inventor)
        self.topspeed = topspeed
        self.steering = steering
        self.lights = lights
        self.navigation = navigation
        self.engine = engine

class Car(Vehicle):
    def __init__(self, make, model, year, inventor, color="White", size="Mid-Size",
                 style="Sedan", engine="V6", price=0, mileage=0, tires="All-Season"):
        super().__init__(inventor, topspeed=120, steering="power", lights="LED",
                         navigation="land", engine=engine)
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.size = size
        self.style = style
        self.tires = tires
        self.mileage = mileage
        self.msrp = price
        self.price = price
        self.bought_for = price

    def short_label(self):
        return f"{self.year} {self.make} {self.model}"

    def full_label(self):
        return (f"{self.year} {self.make} {self.model} | {self.color} {self.style} | "
                f"{self.engine} | {self.mileage:,} mi")

    def display_info(self):
        return (f"{self.year} {self.make} {self.model} — Engine: {self.engine}, "
                f"Color: {self.color}, Style: {self.style}, Price: ${self.price:,.0f}")


# ─────────────────────────────────────────────
#  DISPLAY HELPERS
# ─────────────────────────────────────────────

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def hr(char="─", width=60):
    print(char * width)

def header(title):
    clear()
    hr("═")
    print(f"  🚗  AUTOROW DEALERSHIP SIMULATOR")
    hr("═")
    print(f"  {title}")
    hr()

def pause(msg="  Press Enter to continue..."):
    input(f"\n{msg}")

def fmt(n):
    return f"${n:,.0f}"

def slow_print(text, delay=0.018):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()

def print_car_list(cars, show_price=True, show_trade_val=False, multiplier=1.0):
    if not cars:
        print("  (none)")
        return
    print(f"  {'#':<3} {'Year':<5} {'Make':<12} {'Model':<12} {'Style':<12} {'Color':<9} {'Engine':<5} {'Miles':>8}  {'Price':>10}")
    hr("-")
    for i, car in enumerate(cars, 1):
        p = car.price * multiplier
        tv = p * 0.55
        price_col = fmt(tv) if show_trade_val else fmt(p)
        label = " trade val" if show_trade_val else ""
        print(f"  {i:<3} {car.year:<5} {car.make:<12} {car.model:<12} {car.style:<12} "
              f"{car.color:<9} {car.engine:<5} {car.mileage:>8,}  {price_col:>10}{label}")

def pick_from_list(prompt, length, allow_cancel=True):
    suffix = " (or 0 to cancel)" if allow_cancel else ""
    while True:
        try:
            val = int(input(f"\n  {prompt}{suffix}: "))
            if allow_cancel and val == 0:
                return None
            if 1 <= val <= length:
                return val - 1
            print(f"  Enter a number between 1 and {length}.")
        except ValueError:
            print("  Please enter a number.")


# ─────────────────────────────────────────────
#  DATA
# ─────────────────────────────────────────────

CAR_POOL = [
    Car("Toyota",    "Camry",    2022, "Toyota",    color="Silver", style="Sedan",       engine="V6", price=26000, mileage=22000),
    Car("Honda",     "Civic",    2023, "Honda",     color="Blue",   style="Hatchback",   engine="V4", price=23000, mileage=8000),
    Car("Ford",      "Mustang",  2021, "Ford",      color="Red",    style="Coupe",       engine="V8", price=42000, mileage=35000),
    Car("Chevrolet", "Tahoe",    2024, "Chevrolet", color="Black",  style="SUV",         engine="V8", price=58000, mileage=4000),
    Car("Ram",       "1500",     2023, "Ram",       color="White",  style="Pickup",      engine="V8", price=52000, mileage=12000),
    Car("Mazda",     "MX-5",     2022, "Mazda",     color="Red",    style="Convertible", engine="V4", price=31000, mileage=18000),
    Car("Hyundai",   "Elantra",  2023, "Hyundai",   color="Green",  style="Sedan",       engine="V4", price=21000, mileage=6000),
    Car("BMW",       "3 Series", 2022, "BMW",       color="Grey",   style="Sedan",       engine="V6", price=47000, mileage=28000),
    Car("Jeep",      "Wrangler", 2023, "Jeep",      color="Orange", style="SUV",         engine="V6", price=45000, mileage=14000),
    Car("Tesla",     "Model 3",  2024, "Tesla",     color="White",  style="Sedan",       engine="EV", price=44000, mileage=2000),
    Car("Subaru",    "Outback",  2022, "Subaru",    color="Blue",   style="Wagon",       engine="V4", price=29000, mileage=30000),
    Car("Kia",       "Telluride",2023, "Kia",       color="Black",  style="SUV",         engine="V6", price=38000, mileage=11000),
    Car("Dodge",     "Charger",  2021, "Dodge",     color="Yellow", style="Sedan",       engine="V8", price=35000, mileage=40000),
    Car("Audi",      "Q5",       2023, "Audi",      color="Silver", style="SUV",         engine="V6", price=55000, mileage=9000),
    Car("Nissan",    "Frontier", 2022, "Nissan",    color="Grey",   style="Pickup",      engine="V6", price=33000, mileage=24000),
    Car("Lexus",     "RX 350",   2023, "Lexus",     color="Pearl",  style="SUV",         engine="V6", price=53000, mileage=7000),
    Car("Volkswagen","Jetta",    2022, "VW",        color="White",  style="Sedan",       engine="V4", price=24000, mileage=19000),
    Car("Porsche",   "911",      2021, "Porsche",   color="Silver", style="Coupe",       engine="V6", price=98000, mileage=15000),
]

EVENTS = [
    {"text": "⛽  Gas prices spike! V8 buyers are hesitant.",          "type": "bad",     "effect": "v8_penalty",        "val": 0.85},
    {"text": "🎉  Summer sale frenzy! You earn a deal bonus.",          "type": "good",    "effect": "bonus_pts",         "val": 500},
    {"text": "🏢  Rival lot blowout sale — rival gains 300 pts.",       "type": "bad",     "effect": "rival_pts",         "val": 300},
    {"text": "📉  Market crash! All car values drop 10%.",              "type": "bad",     "effect": "price_mult",        "val": 0.90},
    {"text": "📈  Hot car market! Prices surge 15% this turn.",         "type": "good",    "effect": "price_mult",        "val": 1.15},
    {"text": "🏦  Bank offers 0% loan — your budget +$10,000!",        "type": "good",    "effect": "budget_bonus",      "val": 10000},
    {"text": "🔧  Safety recall on V8 trucks. Buyers are wary.",        "type": "bad",     "effect": "recall_v8",         "val": 0.80},
    {"text": "📱  Influencer posts about convertibles — they're hot!", "type": "good",    "effect": "convertible_bonus", "val": 1.20},
    {"text": "💰  Economic boom! Loyalty bonus awarded.",               "type": "good",    "effect": "bonus_pts",         "val": 400},
    {"text": "👤  Rival snipes a deal — rival gains 250 pts.",          "type": "bad",     "effect": "rival_pts",         "val": 250},
    {"text": "⚡  EV tax rebate! Electric cars are 20% cheaper.",       "type": "good",    "effect": "ev_discount",       "val": 0.80},
    {"text": "😴  Quiet market day. Nothing unusual.",                  "type": "neutral", "effect": "none",              "val": 1.0},
    {"text": "🌧️  Rainy season! SUV demand is up 10%.",                "type": "good",    "effect": "suv_bonus",         "val": 1.10},
    {"text": "🚔  Traffic enforcement crackdown — sports cars slow.",   "type": "bad",     "effect": "coupe_penalty",     "val": 0.88},
    {"text": "🎓  Tax refund season — budget buyers flood the lot.",    "type": "good",    "effect": "budget_bonus",      "val": 5000},
]

BUYER_NAMES = ["Alex","Morgan","Jordan","Riley","Casey","Drew","Taylor","Quinn","Blake","Skyler",
               "Jamie","Avery","Reese","Parker","Dakota","Hayden","Peyton","Cameron","Emery","Logan"]
BUYER_STYLES = ["Sedan","SUV","Pickup","Coupe","Hatchback","Convertible","Wagon"]


# ─────────────────────────────────────────────
#  GAME ENGINE
# ─────────────────────────────────────────────

MAX_TURNS = 15

class Game:
    def __init__(self, role):
        self.role          = role          # "customer" | "dealer"
        self.turn          = 1
        self.score         = 0
        self.rival_score   = 0
        self.budget        = 30000 if role == "customer" else 0
        self.revenue       = 0
        self.garage        = []            # customer's owned cars
        self.inventory     = []            # dealer's lot
        self.event         = None
        self.event_effect  = "none"
        self.event_val     = 1.0
        self.log           = []

        if role == "dealer":
            self.inventory = random.sample(CAR_POOL, 6)
            self.inventory = [Car(c.make, c.model, c.year, c.inventor,
                                  color=c.color, style=c.style, engine=c.engine,
                                  price=c.msrp, mileage=c.mileage) for c in self.inventory]

    # ── price helpers ──────────────────────────

    def effective_price(self, car):
        p = car.msrp - car.mileage * 0.08
        if self.event_effect == "price_mult":      p *= self.event_val
        if self.event_effect == "v8_penalty"   and car.engine == "V8":      p *= self.event_val
        if self.event_effect == "recall_v8"    and car.engine == "V8":      p *= self.event_val
        if self.event_effect == "convertible_bonus" and car.style == "Convertible": p *= self.event_val
        if self.event_effect == "ev_discount"  and car.engine == "EV":      p *= self.event_val
        if self.event_effect == "suv_bonus"    and car.style  == "SUV":     p *= self.event_val
        if self.event_effect == "coupe_penalty" and car.style == "Coupe":   p *= self.event_val
        return max(1000, round(p))

    def trade_value(self, car):
        return round(self.effective_price(car) * 0.55)

    # ── log / rival ────────────────────────────

    def add_log(self, msg):
        self.log.insert(0, msg)
        if len(self.log) > 8:
            self.log.pop()

    def rival_move(self):
        pts = random.randint(80, 260)
        self.rival_score += pts
        self.add_log(f"Rival made a move and scored {pts} pts.")

    # ── event roller ───────────────────────────

    def roll_event(self):
        self.event = random.choice(EVENTS)
        self.event_effect = self.event["effect"]
        self.event_val    = self.event["val"]
        if self.event_effect == "bonus_pts":   self.score        += self.event_val
        if self.event_effect == "rival_pts":   self.rival_score  += self.event_val
        if self.event_effect == "budget_bonus":self.budget       += self.event_val

    # ── score bar ──────────────────────────────

    def score_bar(self):
        total = max(self.score + self.rival_score, 1)
        width = 40
        you_w = int(self.score / total * width)
        riv_w = width - you_w
        bar = "█" * you_w + "░" * riv_w
        return f"  YOU [{bar}] RIVAL"

    # ── status header ──────────────────────────

    def print_status(self, title=""):
        header(title or ("Customer Mode" if self.role == "customer" else "Dealer Mode"))
        print(f"  Turn {self.turn}/{MAX_TURNS}   |   Your Score: {int(self.score)}   |   Rival Score: {int(self.rival_score)}")
        print(self.score_bar())
        if self.role == "customer":
            print(f"  Budget: {fmt(self.budget)}   |   Garage: {len(self.garage)} car(s)")
        else:
            print(f"  Revenue: {fmt(self.revenue)}   |   Inventory: {len(self.inventory)} car(s)")
        hr()
        if self.event:
            tag = "[GOOD]" if self.event["type"]=="good" else "[BAD] " if self.event["type"]=="bad" else "[INFO]"
            print(f"  {tag} {self.event['text']}")
            hr()

    # ── print log ──────────────────────────────

    def print_log(self):
        if self.log:
            hr("·")
            print("  Recent activity:")
            for entry in self.log[:5]:
                print(f"    • {entry}")

    # ── advance ────────────────────────────────

    def advance(self):
        self.event_effect = "none"
        self.event_val    = 1.0
        self.event        = None
        self.turn += 1


# ─────────────────────────────────────────────
#  CUSTOMER TURN
# ─────────────────────────────────────────────

def customer_turn(g: Game):
    g.roll_event()

    # draw 4 random lot cars (exclude ones already in garage by model)
    owned_models = {c.model for c in g.garage}
    pool = [c for c in CAR_POOL if c.model not in owned_models]
    lot = random.sample(pool, min(4, len(pool)))
    lot = [Car(c.make, c.model, c.year, c.inventor, color=c.color, style=c.style,
               engine=c.engine, price=c.msrp, mileage=c.mileage) for c in lot]

    while True:
        g.print_status("Customer Turn")

        print("  ACTIONS:")
        print("  [1] Buy a car from the lot")
        print("  [2] Trade in a car from your garage")
        print("  [3] Trade in + buy (combo deal)")
        print("  [4] View my garage")
        print("  [5] Skip turn  (+20 pts)")
        g.print_log()

        choice = input("\n  Choose action: ").strip()

        if choice == "1":
            customer_buy(g, lot)
            break
        elif choice == "2":
            customer_trade_in(g)
            break
        elif choice == "3":
            customer_combo(g, lot)
            break
        elif choice == "4":
            customer_view_garage(g)
        elif choice == "5":
            g.score += 20
            g.add_log("Turn skipped. +20 pts")
            g.rival_move()
            break
        else:
            print("  Invalid choice.")


def customer_buy(g: Game, lot):
    g.print_status("Buy a Car")
    print("  Available on the lot this turn:\n")
    for i, car in enumerate(lot, 1):
        p = g.effective_price(car)
        saved = car.msrp - p
        print(f"  [{i}] {car.full_label()}")
        print(f"       Asking: {fmt(p)}  (MSRP {fmt(car.msrp)}, you save {fmt(saved)})")
    print()

    idx = pick_from_list("Select a car to buy", len(lot))
    if idx is None:
        return

    car = lot[idx]
    p   = g.effective_price(car)

    if p > g.budget:
        print(f"\n  Not enough budget! You have {fmt(g.budget)}, car costs {fmt(p)}.")
        pause()
        return

    saved = max(0, car.msrp - p)
    pts   = round(saved * 0.05) + 150
    g.budget -= p
    g.score  += pts
    car.bought_for = p
    g.garage.append(car)
    g.add_log(f"Bought {car.short_label()} for {fmt(p)}. +{pts} pts")
    g.rival_move()

    print(f"\n  ✔  Deal done! Bought {car.short_label()} for {fmt(p)}.")
    print(f"     You saved {fmt(saved)} off MSRP — +{int(pts)} pts!")
    pause()


def customer_trade_in(g: Game):
    if not g.garage:
        print("\n  Your garage is empty — nothing to trade in.")
        pause()
        return

    g.print_status("Trade In a Car")
    print("  Your garage:\n")
    for i, car in enumerate(g.garage, 1):
        tv = g.trade_value(car)
        print(f"  [{i}] {car.full_label()}")
        print(f"       Trade-in value: {fmt(tv)}  (bought for {fmt(car.bought_for)})")
    print()

    idx = pick_from_list("Select a car to trade in", len(g.garage))
    if idx is None:
        return

    car = g.garage[idx]
    tv  = g.trade_value(car)
    profit = tv - car.bought_for
    pts = round(max(0, profit) * 0.08) + 100 if profit >= 0 else 50

    g.budget += tv
    g.score  += pts
    g.garage.pop(idx)
    g.add_log(f"Traded in {car.short_label()} for {fmt(tv)}. +{pts} pts")
    g.rival_move()

    print(f"\n  ✔  Traded in {car.short_label()} for {fmt(tv)}. +{int(pts)} pts")
    pause()


def customer_combo(g: Game, lot):
    if not g.garage:
        print("\n  No cars in your garage to trade in.")
        pause()
        return

    g.print_status("Trade In + Buy (Combo)")
    print("  Step 1 — Select your trade-in:\n")
    for i, car in enumerate(g.garage, 1):
        tv = g.trade_value(car)
        print(f"  [{i}] {car.full_label()}  |  Trade val: {fmt(tv)}")
    print()
    ti_idx = pick_from_list("Select your trade-in", len(g.garage))
    if ti_idx is None:
        return

    trade_car = g.garage[ti_idx]
    tv        = g.trade_value(trade_car)

    print(f"\n  Trade-in credit: {fmt(tv)}\n")
    print("  Step 2 — Pick a car to buy:\n")
    for i, car in enumerate(lot, 1):
        p    = g.effective_price(car)
        cost = max(0, p - tv)
        print(f"  [{i}] {car.full_label()}")
        print(f"       Price: {fmt(p)}  |  After trade: {fmt(cost)}")
    print()
    buy_idx = pick_from_list("Select a car to buy", len(lot))
    if buy_idx is None:
        return

    new_car  = lot[buy_idx]
    p        = g.effective_price(new_car)
    out_cost = max(0, p - tv)

    if out_cost > g.budget:
        print(f"\n  Not enough budget! You need {fmt(out_cost)}, have {fmt(g.budget)}.")
        pause()
        return

    saved  = max(0, new_car.msrp - p)
    pts    = round(saved * 0.05) + 200 + 80   # bonus for combo
    g.budget   -= out_cost
    g.score    += pts
    g.garage.pop(ti_idx)
    new_car.bought_for = p
    g.garage.append(new_car)
    g.add_log(f"Combo: traded {trade_car.short_label()}, bought {new_car.short_label()}. +{pts} pts")
    g.rival_move()

    print(f"\n  ✔  Combo deal complete!")
    print(f"     Traded: {trade_car.short_label()} ({fmt(tv)} credit)")
    print(f"     Bought: {new_car.short_label()} (paid {fmt(out_cost)})")
    print(f"     +{int(pts)} pts!")
    pause()


def customer_view_garage(g: Game):
    clear()
    hr("═")
    print("  YOUR GARAGE")
    hr("═")
    if not g.garage:
        print("  (empty)")
    else:
        for i, car in enumerate(g.garage, 1):
            tv = g.trade_value(car)
            print(f"  [{i}] {car.full_label()}")
            print(f"       Bought for: {fmt(car.bought_for)}  |  Current trade val: {fmt(tv)}")
    pause()


# ─────────────────────────────────────────────
#  DEALER TURN
# ─────────────────────────────────────────────

def make_buyers(g: Game):
    buyers = []
    styles = random.choices(BUYER_STYLES, k=3)
    for style in styles:
        name    = random.choice(BUYER_NAMES)
        budget  = random.randint(15, 70) * 1000
        has_ti  = random.random() > 0.4
        trade_car = None
        if has_ti:
            pool = [c for c in CAR_POOL if c.style != style]
            tc   = random.choice(pool)
            trade_car = Car(tc.make, tc.model, tc.year, tc.inventor,
                            color=tc.color, style=tc.style, engine=tc.engine,
                            price=tc.msrp, mileage=tc.mileage)
        buyers.append({"name": name, "want": style, "budget": budget, "trade_in": trade_car})
    return buyers


def dealer_turn(g: Game):
    g.roll_event()
    buyers = make_buyers(g)

    while True:
        g.print_status("Dealer Turn")

        print("  YOUR INVENTORY:\n")
        if not g.inventory:
            print("  (empty — accept trade-ins to restock!)\n")
        else:
            print_car_list(g.inventory)
        hr()
        print("  TODAY'S BUYERS:\n")
        for i, b in enumerate(buyers, 1):
            ti_str = f"  Trade-in: {b['trade_in'].short_label()} ({fmt(g.trade_value(b['trade_in']))})" if b["trade_in"] else "  No trade-in"
            print(f"  [{i}] {b['name']}  —  wants a {b['want']}  |  Budget: {fmt(b['budget'])}")
            print(f"      {ti_str}")
        hr()
        print("  ACTIONS:")
        print("  [1] Sell a car to a buyer")
        print("  [2] Accept a trade-in (without selling)")
        print("  [3] Add car to inventory (buy wholesale)")
        print("  [4] View full inventory details")
        print("  [5] Skip turn  (+20 pts)")
        g.print_log()

        choice = input("\n  Choose action: ").strip()

        if choice == "1":
            if dealer_sell(g, buyers):
                break
        elif choice == "2":
            if dealer_accept_trade(g, buyers):
                break
        elif choice == "3":
            if dealer_buy_wholesale(g):
                break
        elif choice == "4":
            dealer_view_inventory(g)
        elif choice == "5":
            g.score += 20
            g.add_log("Turn skipped. +20 pts")
            g.rival_move()
            break
        else:
            print("  Invalid choice.")


def dealer_sell(g: Game, buyers):
    if not g.inventory:
        print("\n  No cars in inventory to sell.")
        pause()
        return False

    g.print_status("Sell a Car")
    print("  Select a buyer:\n")
    for i, b in enumerate(buyers, 1):
        print(f"  [{i}] {b['name']} — wants {b['want']}, budget {fmt(b['budget'])}")
    print()
    bi = pick_from_list("Select buyer", len(buyers))
    if bi is None:
        return False
    buyer = buyers[bi]

    print(f"\n  {buyer['name']} wants a {buyer['want']} with budget {fmt(buyer['budget'])}.")
    ti_credit = g.trade_value(buyer["trade_in"]) if buyer["trade_in"] else 0
    if ti_credit:
        print(f"  They have a trade-in worth {fmt(ti_credit)}.")
    print(f"\n  Select a car from your inventory to offer:\n")
    print_car_list(g.inventory)
    print()
    ci = pick_from_list("Select car", len(g.inventory))
    if ci is None:
        return False
    car = g.inventory[ci]

    ask      = g.effective_price(car)
    after_ti = max(0, ask - ti_credit)

    print(f"\n  Offering: {car.full_label()}")
    print(f"  Asking:   {fmt(ask)}")
    if ti_credit:
        print(f"  After trade credit: {fmt(after_ti)}")

    # match check
    style_match = car.style.lower() == buyer["want"].lower()
    if not style_match:
        print(f"  ⚠  Warning: {buyer['name']} wants a {buyer['want']}, this is a {car.style}.")

    if after_ti > buyer["budget"]:
        print(f"\n  ✗  {buyer['name']} can't afford this. They need {fmt(after_ti)}, have {fmt(buyer['budget'])}.")
        pause()
        return False

    markup = ask - (car.msrp - car.mileage * 0.08)
    pts    = 200 + max(0, round(markup * 0.1)) + (80 if buyer["trade_in"] else 0) + (100 if style_match else 0)

    g.revenue    += after_ti
    g.score      += pts
    g.inventory.pop(ci)

    if buyer["trade_in"]:
        g.inventory.append(buyer["trade_in"])
        g.add_log(f"Sold {car.short_label()} to {buyer['name']}. Got {buyer['trade_in'].short_label()} as trade-in. +{pts} pts")
    else:
        g.add_log(f"Sold {car.short_label()} to {buyer['name']} for {fmt(after_ti)}. +{pts} pts")

    g.rival_move()
    print(f"\n  ✔  Deal closed with {buyer['name']}! Collected {fmt(after_ti)}. +{int(pts)} pts")
    if style_match:
        print("     +100 bonus pts for matching their preferred style!")
    pause()
    return True


def dealer_accept_trade(g: Game, buyers):
    eligible = [b for b in buyers if b["trade_in"]]
    if not eligible:
        print("\n  No buyers have a trade-in this turn.")
        pause()
        return False

    g.print_status("Accept Trade-In")
    print("  Buyers with trade-ins:\n")
    for i, b in enumerate(eligible, 1):
        tv = g.trade_value(b["trade_in"])
        print(f"  [{i}] {b['name']} offers: {b['trade_in'].full_label()}  |  Value: {fmt(tv)}")
    print()
    idx = pick_from_list("Accept trade-in from", len(eligible))
    if idx is None:
        return False

    b   = eligible[idx]
    tv  = g.trade_value(b["trade_in"])
    pts = 60
    g.inventory.append(b["trade_in"])
    g.score += pts
    g.add_log(f"Accepted trade-in: {b['trade_in'].short_label()} ({fmt(tv)}). +{pts} pts")
    g.rival_move()
    print(f"\n  ✔  Trade-in accepted! {b['trade_in'].short_label()} added to inventory. +{pts} pts")
    pause()
    return True


def dealer_buy_wholesale(g: Game):
    pool = [c for c in CAR_POOL if not any(i.model == c.model for i in g.inventory)]
    if not pool:
        print("\n  No wholesale cars available.")
        pause()
        return False

    g.print_status("Buy Wholesale")
    options = random.sample(pool, min(5, len(pool)))
    print("  Wholesale options (you pay 70% of MSRP):\n")
    for i, car in enumerate(options, 1):
        cost = round(car.msrp * 0.70)
        print(f"  [{i}] {car.full_label()}")
        print(f"       Wholesale cost: {fmt(cost)}  |  Can sell for ~{fmt(car.msrp - car.mileage*0.08)}")
    print()
    idx = pick_from_list("Select car to add to inventory", len(options))
    if idx is None:
        return False

    car  = options[idx]
    cost = round(car.msrp * 0.70)
    c    = Car(car.make, car.model, car.year, car.inventor, color=car.color,
               style=car.style, engine=car.engine, price=car.msrp, mileage=car.mileage)
    c.bought_for = cost
    g.inventory.append(c)
    g.revenue   -= cost
    g.add_log(f"Bought wholesale: {c.short_label()} for {fmt(cost)}")
    g.rival_move()
    print(f"\n  ✔  {c.short_label()} added to inventory for {fmt(cost)}.")
    pause()
    return True


def dealer_view_inventory(g: Game):
    clear()
    hr("═")
    print("  INVENTORY DETAILS")
    hr("═")
    if not g.inventory:
        print("  (empty)")
    else:
        for i, car in enumerate(g.inventory, 1):
            p = g.effective_price(car)
            print(f"  [{i}] {car.full_label()}")
            print(f"       Current market price: {fmt(p)}")
    pause()


# ─────────────────────────────────────────────
#  TITLE / END SCREENS
# ─────────────────────────────────────────────

def title_screen():
    clear()
    hr("═")
    slow_print("  🚗  AUTOROW — DEALERSHIP SIMULATOR  🚗")
    hr("═")
    print("""
  Buy smart. Sell smarter. Outscore the rival.

  RULES:
  • 15 turns. Each turn a random event hits the market.
  • Score points through deal QUALITY, not just quantity.
  • A rival NPC scores every turn you act — stay ahead!
  • Budget limits, recalls, market booms — adapt or lose.

  ROLES:
  [1] Customer  — buy & trade cars, build the best garage
  [2] Dealership — sell inventory, flip trade-ins, crush rivals
    """)
    hr()
    while True:
        choice = input("  Select your role [1/2]: ").strip()
        if choice == "1":
            return "customer"
        elif choice == "2":
            return "dealer"
        else:
            print("  Enter 1 or 2.")


def end_screen(g: Game):
    header("GAME OVER")
    won = g.score > g.rival_score
    if won:
        slow_print("  🏆  YOU WIN! You outscored the rival!")
    else:
        slow_print("  💀  RIVAL WINS. Better luck next time.")
    print()
    print(f"  Your final score : {int(g.score)}")
    print(f"  Rival final score: {int(g.rival_score)}")
    margin = abs(int(g.score - g.rival_score))
    print(f"  Margin           : {margin} pts")
    hr()
    if g.role == "customer":
        print(f"  Budget remaining : {fmt(g.budget)}")
        print(f"  Cars in garage   : {len(g.garage)}")
        if g.garage:
            print()
            for car in g.garage:
                print(f"    • {car.full_label()}")
    else:
        print(f"  Total revenue    : {fmt(g.revenue)}")
        print(f"  Cars in inventory: {len(g.inventory)}")
    hr()

    # score breakdown
    print("  SCORING TIPS:")
    if won:
        print("  • You made smart deals and kept ahead of the rival.")
    else:
        print("  • Buy cars well below MSRP to earn big buy-bonus pts.")
        print("  • Match buyer style preferences for +100 pt bonuses.")
        print("  • Combo trade-in + buy deals earn extra bonus pts.")
    print()


def play_again():
    while True:
        ans = input("  Play again? [y/n]: ").strip().lower()
        if ans == "y":
            return True
        elif ans == "n":
            return False


# ─────────────────────────────────────────────
#  MAIN LOOP
# ─────────────────────────────────────────────

def main():
    while True:
        role = title_screen()
        g    = Game(role)

        while g.turn <= MAX_TURNS:
            if role == "customer":
                customer_turn(g)
            else:
                dealer_turn(g)
            if g.turn <= MAX_TURNS:
                g.advance()

        end_screen(g)
        if not play_again():
            print("\n  Thanks for playing AutoRow. See you on the lot! 🚗\n")
            break


if __name__ == "__main__":
    main()
