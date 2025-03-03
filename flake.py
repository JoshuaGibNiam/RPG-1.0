from fairy import Fairy

class Flake(Fairy):
    def special_ability(self):
        self.hp += 10
        self.defense += 5
        return f"{self.name} uses ability and blooms into a fat-ass snowflake!!!"
    