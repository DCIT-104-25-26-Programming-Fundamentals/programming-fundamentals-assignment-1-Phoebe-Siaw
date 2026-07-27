# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
#
# Build a calculator program that runs in the console and performs basic
# arithmetic operations based on the user's input.
#
# -----------------------------------------------------------------------------
# OPERATIONS YOUR CALCULATOR MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Addition          ( + )    e.g.  10 + 3  =  13
#   2. Subtraction       ( - )    e.g.  10 - 3  =  7
#   3. Multiplication    ( * )    e.g.  10 * 3  =  30
#   4. Division          ( / )    e.g.  10 / 3  =  3.33
#   5. Modulus           ( % )    e.g.  10 % 3  =  1  (remainder)
#   6. Exponentiation    ( ** )   e.g.  2 ** 8  =  256
#   7. Quit
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ============================
#        SIMPLE CALCULATOR
#   ============================
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Modulus
#   6. Exponentiation
#   7. Quit
#   Select an operation (1-7):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Select an operation (1-7): 4
#   Enter first number : 10
#   Enter second number: 3
#   Result: 10 / 3 = 3.33
#
#   Select an operation (1-7): 4
#   Enter first number : 5
#   Enter second number: 0
#   Error: Cannot divide by zero.
#
#   Select an operation (1-7): 7
#   Goodbye!
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Each arithmetic operation MUST be written as its own function.
# - Use a loop so the calculator keeps running until the user selects Quit.
# - Division by zero must be caught and handled with a clear error message
#   (do NOT let the program crash).
# - Division results should be rounded to 2 decimal places.
# - Handle invalid menu choices gracefully.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def add(a, b):
	return a + b


def subtract(a, b):
	return a - b


def multiply(a, b):
	return a * b


def divide(a, b):
	if b == 0:
		raise ZeroDivisionError
	return round(a / b, 2)


def modulus(a, b):
	if b == 0:
		raise ZeroDivisionError
	return a % b


def exponent(a, b):
	return a ** b


def get_number(prompt):
	try:
		return float(input(prompt))
	except ValueError:
		raise


def main():
	while True:
		print("\n============================\n     SIMPLE CALCULATOR\n============================")
		print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Modulus\n6. Exponentiation\n7. Quit")
		choice = input("Select an operation (1-7): ").strip()
		if choice == '7':
			print("Goodbye!")
			break
		if choice not in {'1','2','3','4','5','6'}:
			print("Error: invalid choice.")
			continue
		try:
			a = get_number("Enter first number : ")
			b = get_number("Enter second number: ")
		except ValueError:
			print("Error: please enter numeric values.")
			continue

		try:
			if choice == '1':
				res = add(a, b)
				op = '+'
			elif choice == '2':
				res = subtract(a, b)
				op = '-'
			elif choice == '3':
				res = multiply(a, b)
				op = '*'
			elif choice == '4':
				res = divide(a, b)
				op = '/'
			elif choice == '5':
				res = modulus(a, b)
				op = '%'
			elif choice == '6':
				res = exponent(a, b)
				op = '**'
			print(f"Result: {a} {op} {b} = {res}")
		except ZeroDivisionError:
			print("Error: Cannot divide by zero.")


if __name__ == "__main__":
	main()

