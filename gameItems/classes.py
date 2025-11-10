import weapons
import armors
import skills
class playerType:
    def __init__(self, name: str, strength: int, dexterity: int, constitution: int, accuracy: int, technology: int, magic: int, weapon: str, armor: str, skills: str) -> None:
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.accuracy = accuracy
        self.technology = technology
        self.magic = magic
        self.weapon = weapon
        self.armor = armor
        self.skills = skills
    
    knight = playerType(name="Kinght", strength = 15, dexterity = 14, constitution = 13, accuracy = 12, magic = 10, technology = 8, weapon =  weapons.ironSword, armor = armors.leather)
    
    