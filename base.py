class Character:
    def __init__(self, name, attack, defense):
        self.name = name
        self.hp = 50  # Default HP
        self.attack = attack
        self.defense = defense
        self.weapon = None
        self.armor = None
        self.attack_power = 1
        self.defense_power = 1

    def equip_weapon(self, weapon):
        """Equip a weapon if attack stat meets the minimum requirement"""
        if self.attack >= weapon.min_attack:
            self.weapon = weapon
            print(f"{self.name} equipped {weapon.__class__.__name__} (+{weapon.attack_bonus} attack).")
            self.attack_power += self.weapon.attack_bonus
            return True
        else:
            print(f"⚠ {self.name} does not meet the {weapon.min_attack} attack requirement for {weapon.__class__.__name__}!")
            return False
    def equip_armor(self, armor):
        """Equip armor if defense stat meets the minimum requirement"""
        if self.defense >= armor.min_defense:
            self.armor = armor
            print(f"{self.name} equipped {armor.__class__.__name__} (+{armor.defense_bonus} defense).")
            self.defense_power += armor.defense_bonus
            return True
        else:
            print(f"⚠ {self.name} does not meet the {armor.min_defense} defense requirement for {armor.__class__.__name__}!")
            return False
    def special_ability(self):
        """Placeholder for subclasses to override"""
        pass