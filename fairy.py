from base import *
from equipment import *

class Fairy(Character):
    def __init__(self, name):
        super().__init__(name, attack=5, defense=15)

    def special_ability(self):
        self.hp += 10
        print("Fairy heals herself!!!!!!")


if __name__ == '__main__':
    fart = Fairy("Fart")
    fart.equip_weapon(Dagger())
    print(fart.attack_power)