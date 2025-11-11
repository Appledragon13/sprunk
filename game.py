'''

'''

#important imports
from gameItems import classes

# Pick a class
print("Pick a class from the list")
print("1. Knight")
playerClass = input()

if playerClass == "1" or playerClass.lower() == "knight":
    playerClass = classes.knight
    print(playerClass.name)

# Stats
