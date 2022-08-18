def main():
    userFile = input("File Name: ")
    try:
        with open(userFile) as inFile:
            print("Your file '%s' was found." % (userFile))
            for element in inFile:
                print(element)
        print("Thanks!")
    except FileNotFoundError as e:
        print("Your file '%s' had this error:" %(userFile), e)
    finally:
        print("cock an ball torture B)")


if __name__ == "__main__":
    main()
