counter = 0
userInput = []

while counter < 7:
    singer = input("Enter Musical Artist: ")
    userInput[counter] = singer
    counter = counter + 1

    if singer.lower() == "justin bieber":
        print("No way!")
        counter = counter - 1
        continue
    if singer == "" and counter < 7:
        print("That's less than seven, but OK")
        break

newCounter = 0

while newCounter < len(userInput):
    print(userInput[counter])
    newCounter = newCounter + 1
