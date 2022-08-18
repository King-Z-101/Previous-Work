def main():
    saying = "Long live the King!"
    print(saying)
    while True:
        userInput = input("What word should I search for in the saying? ")
        if userInput == "":
            break
        else:
            if userInput.lower() in saying.lower():
                print("Yes, '" + userInput + "' is found in: Long live the King!")
            else:
                print("I could not find '" + userInput + "' in: Long live the King!")
    print("\nEND OF PROGRAM")


if __name__ == "__main__":
    main()
