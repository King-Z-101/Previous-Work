from datetime import datetime


def main():
    year = input("In what year were you born? ")
    month = input("In what month were you born? ")
    day = input("What day of the month were you born? ")
    time = input("What hour of the day were you born? ")
    bday = datetime(int(year), int(month), int(day), int(time))

    print("Your birthdate and hour of birth is ", bday)


if __name__ == "__main__":
    main()
