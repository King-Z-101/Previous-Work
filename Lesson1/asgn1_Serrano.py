print("Assignment 1" + "\n")

# Ask user for input and store in variables
userName = input("What is your name? ")
userAge = input("What is your age? ")
hoursSlept = input("On average, how many hours do you sleep at night? ")

# Formula used to calculate how many years the user has slept
wastedYears = (float(hoursSlept)/24) * float(userAge)

# Display the years the user has spent sleeping
print("\n" "Hello, " + userName + ".\n" + "You have been unconscious for " + str(wastedYears) + " years!")
