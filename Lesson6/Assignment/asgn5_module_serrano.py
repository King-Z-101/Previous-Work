import random


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
                print(name + ", these are prime earning years.\n")
                break
            else:
                print(name + ", you are a good age to play this game.\n")
                break
        except ValueError:
            print("Warning: " + userAge + " is NOT a valid number.")
            continue

    return age


def loadAnswers():
    answerFileList = []
    while True:
        filename = input("What is the name of the file that contains the Wizards potential answers? ")
        if filename == "answers.txt":
            with open(filename) as NewList:
                for element in NewList:
                    element = element.replace("\n", "")
                    answerFileList.append(element)
            break
        else:
            print("Error: " + filename + " Not Found")
            continue
    return answerFileList  # Never Specified to return the list (step 6)


def askQuestions():
    name = input("What's your name? ")
    age = checkAge(name)
    answerFileList = loadAnswers()  # Weird Wording (step 7)
    numOfQuestions = checkNumofQuestions()
    for i in range(numOfQuestions):
        question = input("\n" + "What's your question? ")
        if question.strip() == "":
            print("You should enter a question")
            continue
        if question.lower().strip() == "bye":
            break
        else:   # Check if u need this else
            wizardFileAnswer = processQuestion(i, question, answerFileList)
            print(wizardFileAnswer)
    print("\nNo more questions for you! \nStop bothering the Wizard!")


def processQuestion(loop_counter, question, answerFileList):
    KeyWordList = ["Who", "What", "Where", "When", "Why", "How"]
    wizardAnswerList = []
    for keyword in KeyWordList:
        if question.startswith(keyword):
            wizardAnswerList = getWizardAnswers(keyword, answerFileList, wizardAnswerList)
            break
    count = len(wizardAnswerList)  # may need to use a different function to get the num of item in the list
    if count > 0:
        random.shuffle(wizardAnswerList)
        wizardFinalAnswer = str(loop_counter+1) + ". The Wizard answers: " + wizardAnswerList[0]
    if count == 0:
        wizardFinalAnswer = str(loop_counter+1) + ". The Wizard answers: I don't know."
    return wizardFinalAnswer  # be weary of this return statement


def getWizardAnswers(keyword, answerFileList, wizardAnswerList):
    for line in answerFileList:
        line = line.split("*")
        line_keyword = line[0]
        line_wizard_answer = line[1]  # confused on this split (how should it be split
        if line_keyword == keyword:
            wizardAnswerList.append(line_wizard_answer)
    return wizardAnswerList
