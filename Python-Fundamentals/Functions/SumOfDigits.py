n = int(input("Enter a number: "))

def sumOfDigits(n):
    sum = 0

    while(n > 0):
        lastDigit = n % 10
        sum += lastDigit
        n = int(n / 10)
    return sum

print("Sum of digits:", sumOfDigits(n))