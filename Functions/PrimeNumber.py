n = int(input("Enter a number: "))

def is_prime(n):
    if n < 2:
        return True
    for i in range(2, n-1):
        if n % i == 0:
            return False

    return True

if is_prime(n):
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")