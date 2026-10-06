while True:
    user_input = input("Enter a number or Quit: ")

    if (user_input.lower() == "quit"):
        print("Thank you!")
        break

    n = int(user_input)

    if (n > 0):
        print("Positive number")
    elif (n < 0):
        print("Negative number")
    else:
        print("Not a positive or negative number")