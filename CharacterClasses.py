import ItemFunc as Item
import ItemClasses
import RNG as RNG

class Character:
    def __init__(self, name):
        self.name = name
        self.stats = {"atk":100, "def":100, "spd":100, "str":100, "vit":100, "int":100, "eva":100, "dex":100, "cha":100, "luk":100}
        self.status = []
        self.inventory = []
        self.skills = []
    
