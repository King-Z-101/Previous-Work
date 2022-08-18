def main():
    stateDict = {}

    with open("states.txt", "r") as infile:
        for statekeyvalue in infile:
            valueList = statekeyvalue.split()
            statecode = valueList[0]
            statename = valueList[1]

            statename = statename.replace("\n", "")

            stateDict[statecode] = statename

        print(stateDict)

    statecodesList = list(stateDict.keys())

    statecodesList.sort()

    for statecode in statecodesList:
        print(statecode + "  " + stateDict[statecode])


if __name__ == "__main__":
    main()
