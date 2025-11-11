import gameItems.weaponsForGame as weaponsForGame
import gameItems.armorsForGame as armorsForGame
# import skills
class classPlayer:
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
    
knight = classPlayer (name="Kinght", strength = 15, dexterity = 14, constitution = 13, accuracy = 12, magic = 10, technology = 8, weapon =  weaponsForGame.ironSword, armor = armorsForGame.leather, skills= "")