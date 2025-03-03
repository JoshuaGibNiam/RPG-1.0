class Character:
    def __init__(self, name, attack, defense):
        self.name = name
        self.hp = 100  # Default HP
        self.attack = attack
        self.defense = defense
        self.weapon = None
        self.armor = None

    def equip_weapon(self, weapon):
        """Equip a weapon if attack stat meets the minimum requirement"""
        if self.attack >= weapon.min_attack:
            self.weapon = weapon
            self.attack += weapon.attack_bonus
            print(f"{self.name} equipped {weapon.__class__.__name__} (+{weapon.attack_bonus} attack).")
            return True
        else:
            print(f"⚠ {self.name} does not meet the {weapon.min_attack} attack requirement for {weapon.__class__.__name__}!")
            return False
    def equip_armor(self, armor):
        """Equip armor if defense stat meets the minimum requirement"""
        if self.defense >= armor.min_defense:
            self.armor = armor
            self.defense += armor.defense_bonus
            print(f"{self.name} equipped {armor.__class__.__name__} (+{armor.defense_bonus} defense).")
            return True
        else:
            print(f"⚠ {self.name} does not meet the {armor.min_defense} defense requirement for {armor.__class__.__name__}!")
            return False
    def special_ability(self):
        """Placeholder for subclasses to override"""
        pass