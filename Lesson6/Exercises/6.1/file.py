

def main():
    firstName = input('First Name: ')
    lastName = input('Last Name: ')
    with open('X6_2.txt', 'w') as outfile:
        outfile.write('Hi ' + firstName + "!\n")
        outfile.write('Your lastname is ' + lastName + '.\n')
    print("X6_2.txt created")


if __name__ == "__main__":
    main()
