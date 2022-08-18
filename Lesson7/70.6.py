from datetime import datetime


def main():
    year = input("In what year were you born? ")
    month = input("In what month were you born? ")
    day = input("What day of the month were you born? ")
    time = input("What hour of the day were you born? ")

    bdatetime = datetime(int(year), int(month), int(day), int(time))
    # someone's birthday and time
    formatted_date = bdatetime.strftime("%B %d, %Y at %H hours (24 hour format)")
    print("\nYour birthdate is", formatted_date)


if __name__ == "__main__":
    main()
