n = int(input("Enter a number: "))

def printDigits(n):
    print("Digits:")
    while(n > 0):
        lastDigit = n % 10
        print(lastDigit)
        n = int(n / 10)

printDigits(n)