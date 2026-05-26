import math

# Arithmetic Functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b


# Scientific Functions
def power(a, b):
    return a ** b

def square_root(a):
    return math.sqrt(a)

def sine(angle):
    return math.sin(math.radians(angle))

def cosine(angle):
    return math.cos(math.radians(angle))

def tangent(angle):
    return math.tan(math.radians(angle))

def logarithm(a):
    return math.log10(a)


# Menu-driven loop
while True:

    print("\n===== SCIENTIFIC CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("10. Logarithm")
    print("11. Exit")

    choice = input("Enter your choice: ")

    try:

        # Addition
        if choice == '1':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result =", add(a, b))

        # Subtraction
        elif choice == '2':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result =", subtract(a, b))

        # Multiplication
        elif choice == '3':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result =", multiply(a, b))

        # Division
        elif choice == '4':
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if b == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print("Result =", divide(a, b))

        # Power
        elif choice == '5':
            a = float(input("Enter base number: "))
            b = float(input("Enter exponent: "))
            print("Result =", power(a, b))

        # Square Root
        elif choice == '6':
            a = float(input("Enter number: "))

            if a < 0:
                print("Error: Cannot calculate square root of negative number.")
            else:
                print("Result =", square_root(a))

        # Sine
        elif choice == '7':
            angle = float(input("Enter angle in degrees: "))
            print("Result =", sine(angle))

        # Cosine
        elif choice == '8':
            angle = float(input("Enter angle in degrees: "))
            print("Result =", cosine(angle))

        # Tangent
        elif choice == '9':
            angle = float(input("Enter angle in degrees: "))
            print("Result =", tangent(angle))

        # Logarithm
        elif choice == '10':
            a = float(input("Enter number: "))

            if a <= 0:
                print("Error: Logarithm undefined for zero or negative numbers.")
            else:
                print("Result =", logarithm(a))

        # Exit
        elif choice == '11':
            print("Calculator Closed.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

    except ValueError:
        print("Error: Please enter valid numeric values.")

    except Exception as e:
        print("An unexpected error occurred:", e)