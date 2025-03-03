from exile import Exile

class Banished(Exile):
    def special_ability(self):
        self.attack_power += 3
        return f"{self.name} transcends to wherever he wants!!!"