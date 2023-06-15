# pig dice game
from random import randint

print("""In this game, players will take turns "rolling" a die to get 30 or more points!
A player can roll as many times as they'd like before they "hold" their score and pass their die to the next opponent.
If, however, they roll a 1, their score resets back to zero and it's their opponent's turn.
Players will continue taking turns until, in the end, the player with a score of 30 or more wins.
""")

while True:
    try:
        number = int(input("Enter the number of players: "))
        break
    except ValueError:
        continue

players = {input(f"Player {name} - Enter your name: ") : 0 for name in range(1, number + 1)}


def start():
    while True:
        for name, score in players.items():
            result = play(name, score)
            if not result:
                return name

def play(name,score):
    while True:
        if score >= 30:
            return False
        turn = input(f"{name} - Press enter to roll die or type 'hold' to end your turn: ").lower()
        if turn == "":
            roll = randint(1,6)
            if roll != 1:
                score += roll
                print(f"Your roll was {roll}. You currently have {score} points!")
            else:
                score = 0
                print("You rolled a 1. You have lost all of your points.")
                return True
        elif turn[0] == "h":
            print(f"You have chosen to hold. You currently have {score} points!")
            players[name] += score
            return True
        else:
            print("Please enter a valid input.")


print(f"Congratulations {start()}! You have won!")

























'''
old player for-loop

players = {}
for i in range(1, number + 1):
    name = input(f"Player {i} - Enter your name: ")
    players[name] = 0

print(players)
'''
