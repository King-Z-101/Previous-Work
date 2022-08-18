def main():
    with open("X6_3.txt", "a") as file:
        while True:
            item = input("Grocery Item: ")
            if item == "":
                break
            file.write(item + '\n')
    with open("X6_3.txt", "r") as Outfile:
        grocerylist = Outfile.read()
        print("Grocery List: \n")
        print(grocerylist, end="")


if __name__ == "__main__":
    main()
