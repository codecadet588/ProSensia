def get_number(prompt):
    while True:
        try:
            value = input(prompt).strip()
            if not value:
                print("Input cannot be empty. Try again.")
                continue
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a number.")

name = input("Enter your name: ").strip()
if not name:
    name = "User"

num1 = get_number("Enter the first number: ")
num2 = get_number("Enter the second number: ")

print(f"\nHello {name}, here are your results:")

print(f"➕ Sum: {num1 + num2}")
print(f"➖ Difference: {num1 - num2}")
print(f"✖ Product: {num1 * num2}")

try:
    print(f"➗ Division: {num1 / num2:.2f}")
except ZeroDivisionError:
    print("➗ Division: Cannot divide by zero.")
