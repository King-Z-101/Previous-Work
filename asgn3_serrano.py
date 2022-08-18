# Defining methods to be used
import sys


def displayGreeting():
    print("\n" + "The Wizard will see you now." + "\n\n" + "OK, let's get started" + "\n")


def askQuestions():
    name = input("What's your name? ")
    try:
        userInput = input("How many Questions do you want to ask the Wizard? ")
        numOfQuestions = int(userInput)
        print("Hey " + name + ", you want to ask the Wizard " + str(numOfQuestions) + " questions.")
        counter = 0
    except ValueError:
        # Show user what they input is not valid
        print("Error: " + str(userInput) + " is not a valid number!")
        sys.exit("PROGRAM TERMINATED WITH ERROR")

    while counter < numOfQuestions:
        question = input("\n" + "What's your question? ")
        counter += 1
        if question.lower().strip() == "bye":
            break
        else:
            processQuestion(counter, question)

    print("\nEND OF PROGRAM")


def processQuestion(loop_counter, question):
    message = str(loop_counter) + ". What kind of question is '" + question + "'?"
    print(message)


def main():
    # Title
    print("Assignment  3\n")
    print("* * The Wizard Game * *\n")

    # Ask user for input and store it
    playGame = input("Do you want to talk to the Wizard? (Yes or No) ")
    playGame = playGame.strip()

    # Call methods based on user input or close the program
    if playGame.lower() == "yes":
        displayGreeting()
        askQuestions()
    else:
        print("The Wizard wants you to go away now!")
        print("\nEND OF PROGRAM")


main()
