def main():
    groceryList = []
    while True:
        item = input("Add a grocery list item: ")
        if item == "":
            groceryList.sort()
            with open("X6_4.txt", "w") as NewList:
                for element in groceryList:
                    NewList.write(element + "\n")
            break
        groceryList.append(item)
    print("\nSorted Grocery List: \n")
    with open("X6_4.txt") as NewList:
        for line in NewList:
            print(line, end="")


if __name__ == "__main__":
    main()
