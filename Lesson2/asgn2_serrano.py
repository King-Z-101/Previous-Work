# Defining methods to be used
def displayGreeting():
    print("\n" + "The Wizard will see you now." + "\n\n" + "OK, let's get started" + "\n")
def askQuestions():
    name = input("What's your name? ")
    question = ""
    while question.lower() != "bye":
        question = input("\n" + "What's your question? ")
        print("What kind of questions is '" + question + "'?")

        if question.lower() == "bye":
            print("\n" + "END OF PROGRAM")

# Title
print("Assignment  2\n")
print("* * The Wizard Game * *\n")

# Ask user for input and store it
playGame = input("Do you want to talk to the Wizard? (Yes or No) ")

# Call methods based on user input or close the program
if playGame == "Yes":
    displayGreeting()
    askQuestions()
else:
    print("The Wizard wants you to go away now!")
    print("\n" + "END OF PROGRAM")
