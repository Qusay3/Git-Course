import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


# print(RPS(2))
# print(RPS.ROCK)
# print(RPS['ROCK'])
# print(RPS.ROCK.value)
# sys.exit()
playagain = True
while playagain:

    playerchoice = input("\nEnter...\n1 for Rock, \n2 for Paper, or \n3 for Scissors\n\n")
    #print(playerchoice)

    player = int(playerchoice)
    if player < 1 | player > 3:
        sys.exit("You must enter 1, 2 or 3.")

    computerchose = random.choice("123")

    computer = int(computerchose)

    #print("")
    # print("You choose" + playerchoice + ".")
    # print("python choose" + computerchose + ".")
    # print("You choose" + str(RPS(player)) + ".")
    # print("python choose" + str(RPS(computer)) + ".")
    print("\nYou choose: " + str(RPS(player)).replace('RPS.', '') + ".")
    print("python choose: " + str(RPS(computer)).replace('RPS.', '') + ".\n")

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

    # emoji = windows + .

    playagain = input("\nPlay again? \nY for yes or\nQ to quit\n\n")

    if playagain.lower() == "y":
        continue
    else:
        print("\n🎉🎉🎉🎉🎉")
        print("Thank you for playing")
        playagain = False
        #Break
sys.exit("Bye! 👋")