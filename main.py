from system import *
from fairy import *
from flake import *
from exile import *
from banished import *

def intinput(message: str, range_stop, range_start=1):
    """Forces user to enter a valid number."""
    answer = input(message)
    while True:
        try:
            answer = int(answer)
            while not answer in list(range(range_start, range_stop+1)):
                answer = input(f"Invalid input, try again: {message}: ")
            return answer
        except ValueError:
            print("Please enter a valid number.")

while True:
    print(f"Welcome to this RPG game! Here we have 4 characters: \n"
          f"1. Fairy\n"
          f"2. Flake\n"
          f"3. Exile\n"
          f"4. Banished")
