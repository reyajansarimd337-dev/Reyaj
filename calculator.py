#!/usr/bin/env python3
"""
A simple Python calculator with basic arithmetic operations.
"""

def add(x, y):
    """Add two numbers."""
    return x + y

def subtract(x, y):
    """Subtract two numbers."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide two numbers."""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def power(x, y):
    """Raise x to the power of y."""
    return x ** y

def square_root(x):
    """Calculate the square root of a number."""
    if x < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return x ** 0.5

def main():
    """Main function to run the calculator."""
    print("=== Python Calculator ===\n")
    
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square Root")
        print("7. Exit")
        
        choice = input("\nEnter choice (1/2/3/4/5/6/7): ").strip()
        
        if choice == '7':
            print("Thank you for using the calculator!")
            break
        
        if choice in ['1', '2', '3', '4', '5']:
            try:
                x = float(input("Enter first number: "))
                y = float(input("Enter second number: "))
                
                if choice == '1':
                    print(f"\n{x} + {y} = {add(x, y)}\n")
                elif choice == '2':
                    print(f"\n{x} - {y} = {subtract(x, y)}\n")
                elif choice == '3':
                    print(f"\n{x} * {y} = {multiply(x, y)}\n")
                elif choice == '4':
                    print(f"\n{x} / {y} = {divide(x, y)}\n")
                elif choice == '5':
                    print(f"\n{x} ^ {y} = {power(x, y)}\n")
            except ValueError as e:
                print(f"\nError: {e}\n")
        
        elif choice == '6':
            try:
                x = float(input("Enter number: "))
                print(f"\n√{x} = {square_root(x)}\n")
            except ValueError as e:
                print(f"\nError: {e}\n")
        
        else:
            print("\nInvalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
