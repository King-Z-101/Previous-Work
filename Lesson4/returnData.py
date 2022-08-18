def main():
    firstName = input("First Name: ")
    lastName = input("Last Name: ")
    newName = format_name(firstName, lastName)
    print(newName)


def format_name(first_name, last_name):
    string = "The formal presentation of your name is: " + last_name + ", " + first_name
    return string


main()

