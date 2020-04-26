import random
import csv

# Variables for users & Get Name of the two players
global p1name
player1= input("Please Enter your player 1's name: ")
global p2name
player2 = input("Please Enter your player 2's name: ")

# Variables for scores
P1RunTotal = 0
P2RunTotal = 0

# Round Variables for each player
rounds = 1
rounds2 = 1

def EvenOdd():
    global total
    global EvenOdd

    if total % 2 == 0:                # even odd tester
        total = total + 10
        print("Even Scored Your new total is " + str(total))

    if total % 2 != 0:
        if total < 5:
            total = 0
            print("under 5 Scored so you scored " + str(total))
            p1name = dice_roll()
            p2name = dice_roll()
        else:
            total = total - 5
            print("Odd Scored new total is " + str(total))

    return EvenOdd

def dice_roll():
    global total
    random.seed()                        # dice adder
    dice1 = int(random.random() * 7)
    dice2 = int(random.random() * 7)
    print("dice one equals", dice1, "dice two equals", dice2)
    total = dice1 + dice2
    print("Total Score is", total)
    return dice_roll

def winner():
    if P1RunTotal == P2RunTotal:
        print("Draw")
        # code to deal with draw will be here
    elif P1RunTotal > P2RunTotal:
        print(str(player1) + " is the Winner")
    else:
        print(str(player2) + " is the Winner")
    return winner

# Rounds for Player 1
while rounds != 6:
    print("\n" + str(player1) + " Round " + str(rounds))

    p1name = dice_roll()
    print(str(player1) + " Rolled " + str(total))
    # Test the Number put odd even tester here
    EvenOdd = EvenOdd
    P1RunTotal = total + P1RunTotal
    # print("Player 1 your score this round was " + str(total))

    rounds = rounds + 1

# Reset Variable dice for player 2
    total = None

# Rounds for Player 2
while rounds2 != 6:
    print("\n" + str(player2) + " Round " + str(rounds2))

    p2name = dice_roll()
    print(str(player2) + " Rolled " + str(total))
    # Test the Number put odd even tester here
    EvenOdd = EvenOdd
    P2RunTotal = total + P2RunTotal
    # print("Player 2 your score this round was " + str(total))

    rounds2 = rounds2 + 1

    # Summarise overall scores
    print("\n" "## ## ## FINAL SCORES ## ## ##")
    print(str(player1) + "'s overall score is " + str(P1RunTotal))
    print(str(player2) + "'s overall score is " + str(P2RunTotal))

    # declare winner
    winner = winner()

    # open results file and send results of player 1 and player 2

    results_file = open("results.txt", "a")
    results_file.write(str(player1) + " score " + str(P1RunTotal) + "\n ")
    results_file.write(str(player2) +  " score " + str(P2RunTotal) + "\n ")

    results_file.close()