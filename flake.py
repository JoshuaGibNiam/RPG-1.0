from fairy import Fairy

class Flake(Fairy):
    def special_ability(self):
        self.hp += 5
        self.defense_power += 5
        print(f"{self.name} uses ability and blooms into a fat-ass snowflake!!!")
