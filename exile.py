from base import *

class Exile(Character):
    def __init__(self, name):
        super().__init__(name, attack=14, defense=6)

    def special_ability(self):
        self.attack_power += 2
        self.defense += 1
        return f"{self.name} increases his attack power and becomes a banana!!!"
