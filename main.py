import random

def guessTheNum():
    playInit = input("Would you like to play a guessing game?[Yes/No]")
    play = playInit.lower()
    win = False

    if play == "yes":
        num = random.randint(1,100)
        guessInt = input("Guess which number I am thinking...")
        guess = int(guessInt)
        while win != True:
            if guess > num:
                print("You guessed too high!")
                guessInt = input("What is your next guess...?")
                guess = int(guessInt)
            elif guess < num:
                print("You guessed too low!")
                guessInt = input("What is your next guess...?")
                guess = int(guessInt)
            else:
                print("You guessed correct!")
                win = True
    else:
        print("Maybe another time?")




guessTheNum()