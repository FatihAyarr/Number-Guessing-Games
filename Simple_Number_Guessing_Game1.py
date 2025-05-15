from random import randint as rd

x = rd(1,10)

guess1 = int(input("Guess a number between 1 and 10! Player 1, Your guess: "))
guess2 = int(input("Guess a number between 1 and 10! Player 2, Your guess: "))


while guess1 != x or guess2 != x:
    guess1 = int(input("Player 1, Your guess: "))
    guess2 = int(input("Player 2, Your guess: "))
    if guess1 == x and guess2 == x:
        print("Congratulations, two correct guesses.")
        a = input("Press 1 to play again and 2 to exit..")
        if a == 1:
            x = rd(1,10)
            continue
        if a == 2:
            break
    elif guess1 == x:
        print("Congratulations, player 1 is the right guess.")
        a = input("Press 1 to play again and 2 to exit..")
        if a == 1:
            x = rd(1,10)
            continue
        if a == 2:
            break
    elif guess2 == x:
        print("Congratulations, player 1 is the right guess.")
        a = input("Press 1 to play again and 2 to exit..")
        if a == 1:
            x = rd(1,10)
            continue
        if a == 2:
            break
        
    