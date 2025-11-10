import random
import game
class weapon:
    def __init__(self, name: str, weapon_type: str, damage_type: str, damage: int, value: int) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage_type = damage_type
        self.damage = damage
        self.value = value

# Tutorial weapons
stick = weapon(name="Stick", weapon_type="melee", damage_type="bludgeon", damage=random.randint(1, 2), value= 1)

basic_bow = weapon(name="Bow", weapon_type="ranged", damage_type="piercing", damage=random.randint(1, 2), value= 1)

wood_sword = weapon(name="Wood Sword", weapon_type="melee", damage_type="slashing", damage=random.randint(1, 2), value= 1)

basic_fist = weapon(name="Fist", weapon_type="melee", damage_type="bludgeon", damage=random.randint(1, 2), value= 0)

# Starter weapon
club = weapon(name="Club", weapon_type="melee", damage_type="bludgeon", damage=random.randint(1, 4), value= 1)

bow = weapon(name="Bow", weapon_type="ramged", damage_type="piercing", damage=random.randint(1, 4), value= 1)