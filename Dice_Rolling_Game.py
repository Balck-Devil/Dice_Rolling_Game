import random

def main():
    player1=0
    player2=0
    rounds=1

    while rounds != 4:
        print("Round - " , str(rounds))
        player1=dice_roll()
        player2=dice_roll()

        print("Player 1 Roll Is :- " , player1)
        print("Player 2 Roll Is :- " , player2)

        if player1==player2:
            print("Draw")
        elif player1 > player2:
            print("Player 1 Won...")
        else:
            print("Player 2 Won...")

        rounds+=1

def dice_roll():
    diceroll=random.randint(1,6)
    return diceroll

main()