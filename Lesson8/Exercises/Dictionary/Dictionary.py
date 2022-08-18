def main():
    statesDict = {}
    with open("text.txt") as NewDictionary:
        for statekeyvalue in NewDictionary:
            valueList = statekeyvalue.split()
            statecode = valueList[0]
            statename = valueList[1]
            statesDict[statecode] = statename
    userKey = input("Enter State Key: ")
    userState = input("Enter State Name: ")
    statesDict[userKey] = userState
    print(statesDict)


if __name__ == "__main__":
    main()
