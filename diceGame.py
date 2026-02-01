import random

def getNames():
    player1 = input("Player 1, enter your name: ")
    player2 = input("Player 2, enter your name: ")
    return player1, player2

def main():
    player1, player2 = getNames()
    roll1 = random.randint(1, 6)
    roll2 = random.randint(1, 6)

    if roll1 > roll2:
        print(f"player {player1} rolls {roll1} and beats {roll2}, Player 1 wins!")
    elif roll2 > roll1:
        print(f"player {player2} rolls {roll2} and beats {roll1}, Player 2 wins!")
    else:
        print(f"player {player1} and player {player2} both roll {roll1}, it's a draw!")
main()