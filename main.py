import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def power(x, y):
    return x ** y

def square_root(x):
    return math.sqrt(x)

def logarithm(x):
    return math.log10(x)

def trigonometry(x):
    x = math.radians(x)
    return math.sin(x), math.cos(x), math.tan(x)

print("Welcome to the Python Calculator!")
print("Please select an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Power")
print("6. Square Root")
print("7. Logarithm")
print("8. Trigonometry")

while True:
    choice = input("Enter your choice (1-8): ")

    if choice in ('1', '2', '3', '4', '5'):
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))

        if choice == '1':
            print(x, "+", y, "=", add(x, y))

        elif choice == '2':
            print(x, "-", y, "=", subtract(x, y))

        elif choice == '3':
            print(x, "*", y, "=", multiply(x, y))

        elif choice == '4':
            if y == 0:
                print("Cannot divide by zero.")
            else:
                print(x, "/", y, "=", divide(x, y))

        elif choice == '5':
            print(x, "^", y, "=", power(x, y))

    elif choice == '6':
        x = float(input("Enter a number: "))
        if x < 0:
            print("Cannot take square root of a negative number.")
        else:
            print("Square root of", x, "=", square_root(x))

    elif choice == '7':
        x = float(input("Enter a number: "))
        if x <= 0:
            print("Cannot take logarithm of a non-positive number.")
        else:
            print("Logarithm base 10 of", x, "=", logarithm(x))

    elif choice == '8':
        x = float(input("Enter an angle in degrees: "))
        sin, cos, tan = trigonometry(x)
        print("Sin(", x, ") =", sin)
        print("Cos(", x, ") =", cos)
        print("Tan(", x, ") =", tan)

    else:
        print("Invalid input. Please try again.")

    restart = input("Do you want to perform another calculation? (y/n)")
    if restart != 'y':
        break
