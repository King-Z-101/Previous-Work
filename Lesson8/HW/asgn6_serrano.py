from datetime import date, datetime


def getCurrentYear():
    currentDate = datetime.now()
    currentYear = currentDate.strftime("%Y")
    return currentYear


def getShortName():
    while True:
        fullname = input("Enter Your Full name: ")
        if fullname == "":
            continue
        else:
            break
    nameLen = len(fullname)
    firstInit = fullname[:1]
    cntr = 0
    spaceFound = False
    for char in fullname:
        cntr += 1
        if char == " ":
            lastSpace = cntr
            spaceFound = True
    if spaceFound == True:
        lastName = fullname[lastSpace:nameLen]
        shortName = firstInit + ". " + lastName
    else:
        shortName = fullname
    return shortName


def getYearFounded():
    while True:
        foundingDate = input("Enter the company's Founding Date in mm/dd/yyyy format: ")
        try:
            formattedDate = datetime.strptime(foundingDate, "%m/%d/%Y")
            yearFounded = formattedDate.strftime("%Y")
            break
        except ValueError:
            print("Founding Date is incorrect format. Try again")
            continue
    return yearFounded


def getEmployeeInfo():
    employeeList = []
    counter = 0
    with open("A8_employees.txt") as employeeReport:
        for employee in employeeReport:
            employee = employee.replace("\n", "")
            employeeList.append(employee)
        employeeList.sort()
        for employee in employeeList:
            counter = counter + 1
            sortedEmployeeList = employee.split("*")
            lastname = sortedEmployeeList[0]
            firstname = sortedEmployeeList[1]
            salary = sortedEmployeeList[2]
            print(str(counter) + ". " + lastname + ", " + firstname + ": $" + salary)
    return employeeList


def promptUser(employeeList):
    while True:
        userInput = input("\nAdd or Remove Employee?  (A, R, or Done): ")
        if userInput.lower().strip() == "done":
            print()
            break
        if userInput.strip() == "":
            print()
            break
        if userInput.lower().strip() == "a" or "r":
            employeeFirstName = input("Enter Employee First Name: ")
            employeeLastName = input("Enter Employee Last Name: ")
            employeeSalary = input("Enter Employee Salary: ")
        else:
            print("Invalid Entry, try again")
            continue
        employeeInfo = employeeLastName + "*" + employeeFirstName + "*" + employeeSalary
        if userInput.lower().strip() == 'a':
            employeeList.append(employeeInfo)
            print(employeeFirstName, employeeLastName + " has been added.")
            continue
        if userInput.lower().strip() == 'r':
            employeeFound = False
            for employee in employeeList:
                if employee == employeeInfo:
                    employeeFound = True
                    employeeList.remove(employee)
                    print(employeeFirstName, employeeLastName + " has been removed.")
            if employeeFound == False:
                print(employeeFirstName, employeeLastName + " is not found and cannot be removed.")
            continue
    newEmployeeList = employeeList
    return newEmployeeList


def createDict(newEmployeeList):
    salaryDict = {}
    with open("A8_employees.txt", "w") as outFile:
        for element in newEmployeeList:
            outFile.write(element + "\n")
    for item in newEmployeeList:
        updatedList = item.split("*")
        employeeKey = updatedList[1] + " " + updatedList[0]
        salaryValue = updatedList[2].replace("\n", "")
        salaryDict[employeeKey] = salaryValue
    employeeKeyList = list(salaryDict.keys())
    employeeKeyList.sort()
    for employee in employeeKeyList:
        print(employee + " - " + "$" + salaryDict[employee])
    return salaryDict


def findEmployee(employeeDict):
    keyList = list(employeeDict.keys())
    while True:
        userInput = input("What is the name you are looking for? ")
        if userInput.lower().strip() == "done":
            print("\nEnd of Program")
            break
        if userInput.strip() == "":
            print("\nEnd of Program")
            break
        if userInput in keyList:
            print("Salary of " + userInput + " is: $" + employeeDict[userInput])
            continue
        if userInput != keyList:
            print("I was unable to find " + userInput)
            continue


def main():
    print("Assignment 6\n")
    userName = getShortName()
    companyDate = int(getYearFounded())
    print("****************")
    print("\nEmployee Report for " + userName + " and Associates.\n")
    currentYear = int(getCurrentYear())
    companyAge = currentYear - companyDate
    print("In Business for " + str(companyAge) + " years\n")
    employeeReport = getEmployeeInfo()
    newList = promptUser(employeeReport)
    newDict = createDict(newList)
    findEmployee(newDict)


if __name__ == "__main__":
    main()
