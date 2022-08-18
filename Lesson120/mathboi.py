import math as m


def main():
    while True:
        try:
            userInput = float(input("Enter a number: "))
            print("# Ceiling:", m.ceil(userInput))
            print("# Floor:", m.floor(userInput))
            print("Rounded #:", round(userInput))
            break
        except ValueError:
            print("Enter a number plz")
            continue


if __name__ == "__main__":
    main()
