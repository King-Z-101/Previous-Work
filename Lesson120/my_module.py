
def my_function():
    print("Hello From My Function!")


def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s" % (username, greeting))


def sum_two_numbers(a, b):
    c = a + b
    return c


def main():
    my_function()
    userInput = input("Name: ")
    greeting = "a warm welcome!"
    my_function_with_args(userInput, greeting)
    print(sum_two_numbers(3, 2))


if __name__ == "__main__":
    main()
