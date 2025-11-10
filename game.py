'''

'''

#important imports
from gameItems import armors
from gameItems import healingItems
from gameItems import misc_equipment
from gameItems import weapons
from gameItems import classes

# Pick a class
print("Pick a class from the list")
print("1. Kingt")
playerClass = input()

if playerClass == "1" or playerClass.lower() == "kight":
    playerClass = classes.knight
    print(playerClass)

# Stats
