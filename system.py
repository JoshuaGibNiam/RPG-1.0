import random

def apply_random_modifier(value):
    """Randomly increases or decreases a value by up to 10%"""
    modifier = random.uniform(-0.1, 0.1)
    return round(value + (value * modifier), 2)

def critical_hit():
    """Returns True if a critical hit occurs (20% chance)"""
    return random.random() < 0.2

def dodge():
    """Returns True if an attack is dodged (15% chance)"""
    return random.random() < 0.15

def fight(character1, character2):
    """Simulates a fair fight between two characters"""
    print(f"\n{character1.name} vs. {character2.name} - Fight Start!\n")

    while character1.hp > 0 and character2.hp > 0:
        # Character 1 attacks
        attack_value = apply_random_modifier(character1.attack_power)

        if critical_hit():
            attack_value = round(attack_value * 1.5, 2)
            print(f"🔥 CRITICAL HIT! {character1.name}'s attack is boosted!")

        if dodge():
            print(f"⚡ {character2.name} dodges the attack!")
        else:
            damage = max(1, round(attack_value - character2.defense, 2))
            character2.hp = round(character2.hp - damage, 2)
            print(f"{character1.name} deals {damage} damage. {character2.name} has {character2.hp} HP left.")

        # Swap turns
        character1, character2 = character2, character1

    # Determine the winner
    winner = character1 if character1.hp > 0 else character2
    print(f"\n🏆 {winner.name} wins the battle!\n")