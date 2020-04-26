import random
# import math

print("Enter player names")
p1name = input()
P1RunTotal = 0

p2name = input()
P2RunTotal = 0

rounds = 1

def EvenOdd():
    global total
    global EvenOdd

    if total % 2 == 0:                # even odd tester
        total = total + 10
        print("Even Scored Your new total is " + str(total))

    if total % 2 != 0:
        if total < 5:
            total = 0
            print("under 5 Scored so you scored", +str(total))

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
    print("your Total is", total)
    return dice_roll

while rounds != 6:            # rounds
    print("Round " + str(rounds))

    p1name = dice_roll()
    print("Player 1 Rolled " + str(total))
    # Test the Number put odd even tester here
    EvenOdd = EvenOdd()
    P1RunTotal = total + P1RunTotal
    print("Player 1 overall score is " + str(P1RunTotal))

    rounds = rounds + 1