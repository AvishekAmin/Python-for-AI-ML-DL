def checkNum(str):
    if(str == 'quit'):
        print("Thank you!")
        return
    else:
        n = int(str)
        if(n > 0):
            print("Positive number")
        elif(n < 0):
            print("Negative number")
        else:
            print("Not a positive or negative number")

        str2 = input("Do you want to continue? (y/n): ")
        if(str2 == 'y'):
            str = input("Enter a number or quit: ")
            checkNum(str)
        else: 
            print("Thank you!")
            return

str = input("Enter a number or quit: ")
checkNum(str)