def main():
    tupleList = (1, 2, 3, 4)
    total = 0
    print("Tuple:\n")
    print(tupleList)

    for i in range(len(tupleList)):
        total = total + tupleList[i]
    print("Tuple Total: " + str(total))


if __name__ == "__main__":
    main()
