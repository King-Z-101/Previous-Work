# Defining methods to be used


def displayGreeting():
    print("\n" + "The Wizard will see you now." + "\n\n" + "OK, let's get started" + "\n")


def checkNumofQuestions():
    try:
        userInput = input("\nHow many Questions do you want to ask the Wizard? ")
        numOfQuestions = int(userInput) + 1
        print("I am giving you a bonus, you can ask " + str(numOfQuestions) + " questions!")
        return numOfQuestions
        # counter = 0
    except ValueError:
        # Show user what they input is not valid
        print("Warning: " + str(userInput) + " is NOT a valid number. I am changing it to 5.")
        numOfQuestions = 5
        return numOfQuestions
        # sys.exit("PROGRAM TERMINATED WITH ERROR")


def checkAge(name):
    while True:
        try:
            userAge = input("What is your age? ")
            age = int(userAge)
            if age < 10 or age > 80:
                print(name + ", please enter a valid age between 10 and 80.")
                continue
            elif 30 < age < 50:
                print(name + ", these are prime earning years.")
                break
            else:
                print(name + ", you are a good age to play this game.")
                break
        except ValueError:
            print("Warning: " + userAge + " is NOT a valid number.")
            continue

    return age


def askQuestions():
    name = input("What's your name? ")
    age = checkAge(name)
    numOfQuestions = checkNumofQuestions()
    for i in range(numOfQuestions):
        question = input("\n" + "What's your question? ")
        if question.strip() == "":
            print("You should enter a question")
            continue
        if question.lower().strip() == "bye":
            break
        else:
            rtnanswer = processQuestion(i, question)
            print(rtnanswer)
    print("\nNo more questions for you! \nStop bothering the Wizard!")
    print("\nEND OF PROGRAM")


def processQuestion(loop_counter, question):
    answer = ""
    if question.startswith("Who"):
        answer = "Who, who... isn't that a sound an owl makes?"
    elif question.startswith("What"):
        answer = "What is the meaning of life?"
    elif question.startswith("How"):
        answer = "How now, brown cow?"
    else:
        answer = "I don't know."
    displayAnswer = str(loop_counter+1) + ". The Wizard answers: " + answer + ""
    return displayAnswer


def main():
    # Title
    print("Assignment  4\n")
    print("* * The Wizard Game * *")

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
