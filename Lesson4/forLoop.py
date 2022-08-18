def main():
    print("My favorite artists", "\n")
    userInput = ""
    artist = ""

    for i in range(1, 4):
        userInput = input("Enter Music Artist: ")
        artist = artist + str(i) + ". " + userInput + "\n"

    print(artist)


main()
