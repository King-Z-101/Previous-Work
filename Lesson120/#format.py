def main():
    try:
        mystr = input("Enter a Number: ")
        mynum = int(mystr)
        whatisit = "integer"
    except ValueError:
        #It is Not an Integer so try...

        try:
            mynum = float(mystr)
            whatisit = "float"
        except ValueError:
            print("Not a Float")
            return

    if whatisit == "integer":
        print("Integer: ", end="")
        print("{:,}".format(mynum))
    else:
        print("Float: ", end="")
        print("{:,.2f}".format(mynum))

    print("End of program")


if __name__ == "__main__":
    main()
