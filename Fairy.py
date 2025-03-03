from base import *
from equipment import *

class Fairy(Character):
    def __init__(self, name):
        super().__init__(name)
        self.attack_power = 4
        self.defense = 16
        self.weapon = None