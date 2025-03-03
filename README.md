# RPG Character Ecosystem

---

## Project Overview
The **RPG Character Ecosystem** is a Python-based role-playing game (RPG).
The goal of this project is to create a dynamic battle system where characters, weapons, and 
armor interact through predefined rules.

---

## Usage

### Character System
1. You must create one of the four characters as shown. Enter the right input(1-4), 
and it'll be alright.

### Equipment System
| **Weapon**      | **Attack Bonus** | **Min Attack Required** |
|----------------|----------------|----------------------|
| Dagger        | +2             | 5                    |
| Sword         | +4             | 8                    |
| Greatsword    | +6             | 12                   |
| Staff         | +3             | 6                    |

| **Armor**      | **Defense Bonus** | **Min Defense Required** |
|---------------|------------------|----------------------|
| Leather      | +2               | 5                    |
| Chainmail    | +4               | 8                    |
| Plate Armor  | +6               | 12                   |
| Wizard Robes | +3               | 6                    |

1. Equip a weapon and an armor for each of the characters. Enter (1-4)

### Battle System
A universal **fight function** ensures balanced combat:
- **Turn-based attack system**
- **Damage formula**: `attack - opponent.defense (min 1)`
- **Random Modifiers**:
  - **Attack fluctuation**: ±10%
  - **Critical hits**: 20% chance (1.5x damage)
  - **Dodge chance**: 15% (avoid damage)

---

## Project Structure
```
RPG_Character_Ecosystem/
│── main.py            # Main execution script
│── base.py            # Base Character class
│── |-fairy.py         
    |-exile.py         #Custom RPG subclasses
    |-flake.py         #
    |-banished.py      
│── equipment.py       # Weapons and armor classes
│── fight.py           # Battle system implementation
│── README.md          # Project documentation
```

---

## Installation
Clone this repository and navigate to the project folder:
```sh
git clone https://github.com/yourusername/RPG_Character_Ecosystem.git
cd RPG_Character_Ecosystem
```
### Prerequisites
Ensure you have **Python 3.7+** installed.
### Running the Project
Execute the main script to test character interactions and battles:
```sh
python main.py
```

---

## Credits
Author: Joshua Niam [JoshuaGibNiam](https://github.com/JoshuaGibNiam)

---
Monday, 3rd of March 2025, 6:13 p.m.
