from system import *
from fairy import *
from flake import *
from exile import *
from banished import *
from equipment import *
def intinput(message: str, range_stop, range_start=1):
    """Forces user to enter a valid number."""
    while True:
        try:
            answer = int(input(message))  # Get user input
            if range_start <= answer <= range_stop:
                return str(answer)  # Return the valid integer
            else:
                print(f"Invalid input, please enter a number between {range_start} and {range_stop}.")
        except ValueError:
            print("Please enter a valid number.")

CHARACTERS = {"1": Fairy,  #Constant dicts shall be used later on
              "2": Flake,
              "3": Exile,
              "4": Banished}
WEAPON = {"1": Dagger,
          "2": Sword,
          "3": Greatsword,
          "4": Staff}
ARMOR = {"1": Chainmail,
         "2": PlateArmor,
         "3": Leather,
         "4": WizardRobe}
while True:
    print(f"Welcome to this RPG game! Here we have 4 characters: \n"
          f"1. Fairy\n"
          f"2. Flake\n"
          f"3. Exile\n"
          f"4. Banished")

    char1 = intinput("Choose your first character (1-4): ", 4)
    char1 = CHARACTERS[char1]("Character 1")

    print(f"Character 1 has {char1.attack} points.\n"
          f"1. Dagger +2 Bonus, Cost: 5\n"
          f"2. Sword +4 Bonus, Cost: 8\n"
          f"3. Greatsword +6 Bonus, Cost: 12\n"
          f"4. Staff +3 Bonus, Cost: 6")
    char1weapon = intinput("Choose your weapon: ", 4)
    char1weapon = WEAPON[char1weapon]()
    while not char1.equip_weapon(char1weapon):
        char1weapon = intinput("Choose your weapon: ", 4)
        char1weapon = WEAPON[char1weapon]()
    print(f"Character 1 has {char1.defense} points.\n"
          f"1. Leather +2 Bonus, Cost: 5\n"
          f"2. Chainmail +4 Bonus, Cost: 8\n"
          f"3. Plate Armor +6 Bonus, Cost: 12\n"
          f"4. Wizard's Robes +3 Bonus, Cost: 6")
    char1armor = intinput("Choose your armor: ", 4)
    char1armor = ARMOR[char1armor]()
    while not char1.equip_armor(char1armor):
        char1armor = intinput("Choose your armor: ", 4)
        char1armor = ARMOR[char1armor]()

    print(f"1. Fairy\n"  #Same with character 2
          f"2. Flake\n"
          f"3. Exile\n"
          f"4. Banished")
    char2 = intinput("Choose your second character (1-4): ", 4)
    char2 = CHARACTERS[char2]("Character 2")
    print(f"Character 1 has {char1.attack} points.\n"
          f"1. Dagger +2 Bonus, Cost: 5\n"
          f"2. Sword +4 Bonus, Cost: 8\n"
          f"3. Greatsword +6 Bonus, Cost: 12\n"
          f"4. Staff +3 Bonus, Cost: 6")
    char2weapon = intinput("Choose your weapon: ", 4)
    char2weapon = WEAPON[char2weapon]()
    while not char2.equip_weapon(char2weapon):
        char2weapon = intinput("Choose your weapon: ", 4)
        char2weapon = WEAPON[char2weapon]()
    print(f"Character 1 has {char2.defense} points.\n"
          f"1. Leather +2 Bonus, Cost: 5\n"
          f"2. Chainmail +4 Bonus, Cost: 8\n"
          f"3. Plate Armor +6 Bonus, Cost: 12\n"
          f"4. Wizard's Robes +3 Bonus, Cost: 6")
    char2armor = intinput("Choose your armor: ", 4)
    char2armor = ARMOR[char2armor]()
    while not char2.equip_armor(char1armor):
        char2armor = intinput("Choose your armor: ", 4)
        char2armor = ARMOR[char2armor]()

    print("Fight starting....")
    winner = fight(char1, char2)
    print(f"{winner} is the winner!!!!! HOOORAAYYYYY")
    desire = intinput("Would you like to play again? (1. y/2. n)", 2)
    if desire == 2:
        print("Thank you for playing!")
        break
