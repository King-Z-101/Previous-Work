def main():
    userSentence = input("Enter a sentence: ")

    print(userSentence, "\n")
    while True:
        searchWord = input("Enter a word to look for: ")
        if userSentence.startswith(searchWord):
            print("Your sentence does start with '" + searchWord + "'")
        elif userSentence.endswith(searchWord):
            print("Your sentence does end with '" + searchWord + "'")
        else:
            print("You sentence does not start with '" + searchWord + "'")
            print("You sentence does not end with '" + searchWord + "'")
        if searchWord.lower().strip() == 'quit':
            break
    print("\nEnd of Program")


main()

