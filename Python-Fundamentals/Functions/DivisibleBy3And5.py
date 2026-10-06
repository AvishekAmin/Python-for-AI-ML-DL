start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

def printNum(start, end):
    for i in range(start, end+1):
        if ((i % 3 == 0) and (i % 5 == 0)):
            print(i)
    return

print("Printing all numbers from", start, "to", end, "that are divisible by both 3 and 5")
printNum(start, end)
