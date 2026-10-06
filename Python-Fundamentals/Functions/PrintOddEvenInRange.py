start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

def printOdd(start, end):
    for i in range(start, end+1):
        if(i % 2 != 0):
            print(i)

def printEven(start, end):
    for i in range(start, end+1):
        if(i % 2 == 0):
            print(i)

print("Printing odd numbers between", start, "and", end)
printOdd(start, end)
print("Printing even numbers between", start, "and", end)
printEven(start, end)