userName = input("Name: ")
userAge = input("Age: ")
newAge = round(float(userAge) + 10)
message = "Hello " + userName + "." + \
          "\n" + "You say you are " + str(userAge) + ", but I bet you are " + str(newAge) + "!"
print(message)

# print("Hi", userName)
