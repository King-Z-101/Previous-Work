print("Tools in Kit\n")

tool = ""
spaceKey = False

while spaceKey == False:
    tool = input("Enter a tool (or press Enter to quit): ")
    print("Tool is:", tool)
    if tool.lower() == "":
        print("\nEnd of list")
        spaceKey = True