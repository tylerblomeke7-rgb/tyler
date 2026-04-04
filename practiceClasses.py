# IDEA 1: Add combat methods to the player class
# - attack(target) - reduces enemy HP based on weapon damage
# - take_damage(amount) - reduces self HP, checks if HP <= 0 (game over)
# - heal(amount) - increases HP (useful for friend class)
# - use_item(item) - applies item effects from inventory
# This teaches: methods, object state changes, logic within classes

# IDEA 2: Create an Item class hierarchy
# - Item (base class): name, value, description
# - Weapon (inherits Item): damage, attack_bonus
# - Potion (inherits Item): healing_amount, effect_type
# - Armor (inherits Item): defense_bonus, durability
# This teaches: extending inheritance, composition (items in inventory)

class player():
    def __init__(self, HP, weapon, house, vehicle, inventory):
        self.HP = HP
        self.weapon = weapon
        self.house = house
        self.vehicle = vehicle
        self.inventory = inventory
    
    def attackPlayer(self, target):
        # Check if the target is an instance of the enemy class or NPC
        if isinstance(target, enemy) or isinstance(target, NPC):
            print(f"Before attack: {target.__class__.__name__} HP = {target.HP}")
            target.HP -= 10
            print(f"After attack: {target.__class__.__name__} HP = {target.HP}")
        else:
            print(f"Cannot attack {target.__class__.__name__} - not an enemy or NPC!")
# - 
    def healplayer(self, target):
        # Check if the healer is a friend or NPC
        if isinstance(self, friend) or isinstance(self, NPC):
            print(f"Before heal: {target.__class__.__name__} HP = {target.HP}")
            target.HP += 10
            print(f"After heal: {target.__class__.__name__} HP = {target.HP}")
        else:
            print(f"{self.__class__.__name__} cannot heal - not a friend or NPC!")
         

class enemy(player):
    def __init__(self, HP, weapon, house, vehicle, inventory, attack):
        super().__init__(HP, weapon, house, vehicle, inventory)
        self.attack = attack

    def attack_player(self, target):
        # Enemy attacks the target (usually player)
        print(f"Before enemy attack: {target.__class__.__name__} HP = {target.HP}")
        target.HP -= self.attack
        print(f"After enemy attack: {target.__class__.__name__} HP = {target.HP}")

class friend(player):
    def __init__(self, HP, weapon, house, vehicle, inventory, healing):
        super().__init__(HP, weapon, house, vehicle, inventory)

        self.healing = healing

class NPC(player):
    def __init__(self, HP, weapon, house, vehicle, inventory, attack, healing):
        super().__init__(HP, weapon, house, vehicle, inventory)

        self.attack = attack
        self.healing = healing    

tyler = player(100, "sword", "cottage", "car", [])
bad_guy = enemy(50, "axe", "cave", "none", [], 15)
good_guy = friend(80, "staff", "house", "bike", [], 20)
neutral_guy = NPC(70, "dagger", "inn", "horse", [], 12, 18)

print("=== Initial HP ===")
print(f"Player HP: {tyler.HP}")
print(f"Enemy HP: {bad_guy.HP}")
print(f"Friend HP: {good_guy.HP}")
print(f"NPC HP: {neutral_guy.HP}")
print()

print("=== Simulation Start ===")
# Player attacks enemy
tyler.attackPlayer(bad_guy)
print()

tyler.attackPlayer(good_guy)

# Friend heals player
good_guy.healplayer(tyler)
print()

# Extra: Enemy attacks player back
bad_guy.attack_player(tyler)
print()

# Extra: NPC heals enemy
neutral_guy.healplayer(bad_guy)
print()

print("=== Final HP ===")
print(f"Player HP: {tyler.HP}")
print(f"Enemy HP: {bad_guy.HP}")
print(f"Friend HP: {good_guy.HP}")
print(f"NPC HP: {neutral_guy.HP}")