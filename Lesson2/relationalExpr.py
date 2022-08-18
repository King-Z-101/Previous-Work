userGuess = input("Guess a number between 1 and 7: ")
tryAgain = True
while tryAgain == True:
    if int(userGuess) == 3:
        print("You guessed correctly!")
        tryAgain = False

    if int(userGuess) < 3:
        message = "Sorry, that's too low"

    if int(userGuess) > 3:
        message = "Sorry, that's too high"

    if int(userGuess) >= 8:
        message = "I said to pick a number between 1 and 7!"

    if tryAgain == True:
        print(message)
        userGuess = input("Guess a number between 1 and 7: ")

