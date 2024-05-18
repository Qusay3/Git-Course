import sys
import random
from enum import Enum

game_count = 0

playagain = True
while playagain:
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerchoice = input("\nEnter...\n1 for Rock, \n2 for Paper, or \n3 for Scissors\n\n")

    if playerchoice not in ["1", "2", "3"]:
        print("You must enter 1, 2 or 3.")
        continue

    player = int(playerchoice)
    computerchose = random.choice("123")
    computer = int(computerchose)

    print("\nYou choose: " + str(RPS(player)).replace('RPS.', '').title() + ".")
    print("Python chooses: " + str(RPS(computer)).replace('RPS.', '').title() + ".\n")

    if player == 1 and computer == 3:
        print("🏆 You win!")
    elif player == 2 and computer == 1:
        print("🏆 You win!")
    elif player == 3 and computer == 2:
        print("🏆 You win!")
    elif player == computer:
        print("😲 Tie game!")
    else:
        print("🐍 Python wins!")

    global game_count
    game_count += 1
    print("\nGame count: " + str(game_count))

    print("\nPlay again?")
    while True:
        playagain= input("\nY for yes or \nQ to quit.\n")
        if playagain.lower() not in ("y", "q"):
            continue
        else:
            print("\n🎉🎉🎉🎉🎉")
            print("Thank you for playing")
            playagain = False
            break

sys.exit("Bye! 👋")
