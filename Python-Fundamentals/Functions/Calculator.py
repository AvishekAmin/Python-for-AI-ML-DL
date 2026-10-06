a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
ch = input("Enter operator (+, -, *, /, %, **): ")

def calculator(a, b, ch):
    match ch:
        case "+":
            print(a, ch, b, "=", (a + b))
        case "-":
            print(a, ch, b, "=", (a - b))
        case "*":
            print(a, ch, b, "=", (a * b))
        case "/":
            print(a, ch, b, "=", (a / b))
        case "%":
            print(a, ch, b, "=", (a % b))
        case "**":
            print(a, ch, b, "=", (a ** b))

calculator(a, b, ch)