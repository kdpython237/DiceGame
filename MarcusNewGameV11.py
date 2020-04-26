import random
import csv

# Variables for users & Get Name of the two players
global p1name
player1 = input("Please Enter player 1's name: ")
global p2name
player2 = input("Please Enter player 2's name: ")

# Variables for scores
P1RunTotal = 0
P2RunTotal = 0

# Round Variables for each player
rounds = 1
rounds2 = 1

def dice_roll():
    global total
    random.seed()                        # dice adder
    dice1 = int(random.random() * 7)
    dice2 = int(random.random() * 7)
    print("dice one equals", dice1, "dice two equals", dice2)
    total = dice1 + dice2
    print("Total Score is" + '\t', + total)
    return dice_roll

def EvenOdd():
    global total
    global EvenOdd
    if total % 2 == 0:                # even odd tester
        total = total + 10
        print("Even Scored Your new total is " + '\t' + str(total))
    if total % 2 != 0:
        if total < 5:
            total = 0
            print("under 5 Scored so you scored " + '\t' + str(total))
        else:
            total = total - 5
            print("Odd Scored new total is " + '\t' + str(total))
    return EvenOdd

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
    print("\n" + str(player1) + " Round " + '\t' + str(rounds))
    p1name = dice_roll()
    print(str(player1) + " Rolled " + '\t' + str(total))
    # Test the Number put odd even tester here
    EvenOdd = EvenOdd()
    P1RunTotal = total + P1RunTotal
    rounds = rounds + 1

# Reset Variable dice for player 2
    total = None

# Rounds for Player 2
while rounds2 != 6:
    print("\n" + str(player2) + " Round " + '\t' + str(rounds2))
    p2name = dice_roll()
    print(str(player2) + " Rolled " + '\t' + str(total))
    EvenOdd = EvenOdd()
    P2RunTotal = total + P2RunTotal
    rounds2 = rounds2 + 1

if rounds and rounds2 == 6:

    # Summarise overall scores
    print("\n",)
    print("\n" "## ## FINAL SCORES FROM THE LAST GAME ## ##")
    print(str(player1) + "'s overall score is " + '\t' + str(P1RunTotal))
    print(str(player2) + "'s overall score is " + '\t' + str(P2RunTotal))

    # declare winner
    print("\n" "## ## GAME RESULT ## ##")
    winner = winner()

    # open results file and send results of player 1 and player 2
    results_file = open("results.txt", "a")
    results_file.write(str(P1RunTotal) +'\t '+ str(player1) + "\n ")
    results_file.write(str(P2RunTotal) +'\t '+ str(player2) + "\n ")
    results_file.close()

    # Open file in read mode used shortcut fr for file read
    #create some space between the last game and the results
    print("\n")
    fr =open('results.txt', 'r')
    readthefile = fr.readlines()
    #Sort the file largest to smallest
    sortedData =sorted(readthefile,reverse=True)

    print('      Top 5 Scores')
    print(' Position , Points,\t Name')

    for line in range(5):
        print(str(line+1) +'\t '+str(sortedData[line]))