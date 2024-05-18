import sys
import random
from enum import Enum

def rps():
    game_count = 0
    plyer_wins = 0
    python_wins = 0

    while True:  # Loop added to allow playing multiple times
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input("\nEnter...\n1 for Rock, \n2 for Paper, or \n3 for Scissors\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print("You must enter 1, 2, or 3.")
            continue  # Restart the loop if input is invalid

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

        game_count += 1
        print("\nGame count: " + str(game_count))

        while True:
            playagain = input("\nPlay again? (Y for yes, Q to quit): ").strip().lower()
            if playagain not in ("y", "q"):
                continue
            else:
                break  # Exit the inner loop if input is valid

        if playagain == 'q':
            break  # Exit the outer loop if user chooses to quit

    print("\n🎉🎉🎉🎉🎉")
    print("Thank you for playing")
    sys.exit("Bye! 👋")

rps()
