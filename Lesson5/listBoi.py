def removeboy(newlist):
    counter = 1
    while True:
        answer = input("Enter an item to remove from the list: ")
        if answer == "":
            break
        else:
            newlist.remove(answer)
    print("\nNew List:\n")
    for i in newlist:
        print(str(counter) + ". " + i)
        counter += 1


def main():
    userList = []
    counter = 1
    while True:
        item = input("Enter an item to add to list: ")
        if item == "":
            break
        else:
            userList.append(item)
    print("\nMy list:\n")
    for item in userList:
        print(str(counter) + ". " + item)
        counter += 1
    removeboy(userList)
    print("\nEND OF PROGRAM")


if __name__ == "__main__":
    main()
