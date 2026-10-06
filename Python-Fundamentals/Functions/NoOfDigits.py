n = int(input("Enter a number: "))

def noOfDigits(n):
    noOfDigits = 0

    while(n > 0):
        lastDigit = n % 10
        noOfDigits += 1
        n = int(n / 10)
    return noOfDigits

print("Number of digits:", noOfDigits(n))