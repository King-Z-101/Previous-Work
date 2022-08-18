def main():
    myList = []
    while True:
        userInput = input("Enter an item to add to list: ")
        if userInput == "":
            break
        else:
            myList.append(userInput)
    myList.sort()
    sorted_list = sorted(myList, key=str.lower)
    print("MyList Sorted:\n")
    for item in sorted_list:
        print(item)


if __name__ == "__main__":
    main()
