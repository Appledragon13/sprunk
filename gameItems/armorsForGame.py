class armor:
    def __init__(self, name: str, defense: int, resitance: str, invulnerability: str) -> None:
        self.name = name
        self.defense = defense
        self.resitance = resitance
        self.invulnerability = invulnerability
        
leather = armor(name = "Leather Armor", defense = 2, resitance= "None", invulnerability="None")