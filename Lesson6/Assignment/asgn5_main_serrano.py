import asgn5_module_serrano as module

print("Assignment  5")
print("* * The Wizard Game * *\n")


def main():
    playGame = input("Do you want to talk to the Wizard? (Yes or No) ")
    if playGame.lower().strip() == "yes":
        module.displayGreeting()
        module.askQuestions()
    else:
        print("The Wizard wants you to go away now!")
        print("\nEND OF PROGRAM")


if __name__ == "__main__":
    main()
