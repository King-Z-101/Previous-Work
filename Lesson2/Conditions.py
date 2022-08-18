userGuess = input("Guess a number between 1 and 7: ")

message = ""

if int(userGuess) == 3:
    message = "You guessed correctly!"
else:
    message = "Sorry, that's not the number I was looking for."
print(message)
