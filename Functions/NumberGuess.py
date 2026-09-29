decided_num = 32

while True:
    n = int(input("Enter a number: "))
    if(n > decided_num):
        print("Too high")
    elif(n < decided_num):
        print("Too low")
    else:
        print("Correct!")
        break