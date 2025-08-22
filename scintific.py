import math

def scientific_calculator():
    print("===== SCIENTIFIC CALCULATOR =====")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Square root (sqrt)")
    print("7. Logarithm (log base 10)")
    print("8. Natural Logarithm (ln)")
    print("9. Trigonometric functions (sin, cos, tan)")
    print("10. Factorial (!)")
    print("11. Exit")

    while True:
        choice = input("\nEnter operation: ")

        # Exit condition
        if choice == "11":
            print("Exiting Calculator...")
            break

        # Binary operations (+, -, *, /, ^)
        if choice in ["1", "2", "3", "4", "5"]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                print(f"Result: {a+b}")
            elif choice == "2":
                print(f"Result: {a-b}")
            elif choice == "3":
                print(f"Result: {a*b}")
            elif choice == "4":
                if b != 0:
                    print(f"Result: {a/b}")
                else:
                    print("Error: Division by zero!")
            elif choice == "5":
                print(f"Result: {math.pow(a, b)}")

        # Unary operations
        elif choice == "6":  # Square root
            a = float(input("Enter number: "))
            print(f"Result: {math.sqrt(a)}")

        elif choice == "7":  # Log base 10
            a = float(input("Enter number: "))
            print(f"Result: {math.log10(a)}")

        elif choice == "8":  # Natural log
            a = float(input("Enter number: "))
            print(f"Result: {math.log(a)}")

        elif choice == "9":  # Trigonometric functions
            a = float(input("Enter angle in degrees: "))
            rad = math.radians(a)
            print(f"sin({a}) = {math.sin(rad)}")
            print(f"cos({a}) = {math.cos(rad)}")
            print(f"tan({a}) = {math.tan(rad)}")

        elif choice == "10":  # Factorial
            a = int(input("Enter integer: "))
            if a >= 0:
                print(f"Result: {math.factorial(a)}")
            else:
                print("Error: Factorial of negative number not defined!")

        else:
            print("Invalid choice! Please try again.")

# Run calculator
scientific_calculator()
