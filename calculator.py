import math

print("===== FULL FLEDGED CALCULATOR =====")
print("Select operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%)")
print("6. Power (^)")
print("7. Square Root (√)")
print("8. Exit")

while True:
    choice = input("\nEnter choice (1-8): ")

    if choice == "1":   # Addition
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result =", a + b)

    elif choice == "2":  # Subtraction
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result =", a - b)

    elif choice == "3":  # Multiplication
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        print("Result =", a * b)

    elif choice == "4":  # Division
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if b != 0:
            print("Result =", a / b)
        else:
            print("Error: Division by zero!")

    elif choice == "5":  # Modulus
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        if b != 0:
            print("Result =", a % b)
        else:
            print("Error: Division by zero!")

    elif choice == "6":  # Power
        a = float(input("Enter base: "))
        b = float(input("Enter exponent: "))
        print("Result =", a ** b)

    elif choice == "7":  # Square Root
        a = float(input("Enter number: "))
        if a >= 0:
            print("Result =", math.sqrt(a))
        else:
            print("Error: Cannot find square root of negative number!")

    elif choice == "8":  # Exit
        print("Exiting Calculator...")
        break

    else:
        print("Invalid Input! Please choose a valid option.")
