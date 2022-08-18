try:
    userAge = int(input("Enter Age: "))
    print("Age = " + str(userAge) + ". Thanks")
except ValueError:
    print("Invalid Integer. Try Again")
