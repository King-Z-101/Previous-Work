def main():
    firstname = input("First Name: ")
    lastname = input("Last Name: ")
    formalname(lastname, firstname)


def formalname(last, first):
    message = "The formal presentation of your name is: " + last + ", " + first
    print(message)


if __name__ == "__main__":
    main()
