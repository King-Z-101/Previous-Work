import sys


def main():
    userInput = ""

    try:
        userInput = input("Pick a number between 1 - 7: ")
        numberOne = int(userInput.strip())

        if numberOne == 3:
            print("You guessed correctly!")

        elif numberOne < 1 or numberOne > 7:
            print("I said to pick a number between 1 and 7!")

    except ValueError:
        sys.exit("Error: " + userInput + " is not a valid input.")

    try:
        userInput = input("Let's try this again. Pick a number between 1 - 7: ")
        numberTwo = int(userInput.strip())
        if numberTwo == 5 and numberOne == 3:
            print("You guessed the 2nd number correctly, and guessed both numbers correctly!")
        elif numberTwo == 5 and numberOne != 3:
            print("You guessed the 2nd number correctly!")
            print("Well you can't win 'em all!")
    except ValueError:
        sys.exit("Error: " + userInput + " is not a valid input.")


main()
