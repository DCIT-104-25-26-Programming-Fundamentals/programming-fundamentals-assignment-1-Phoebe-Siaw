# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def sum_numbers(numbers):
	total = 0
	for num in numbers:
		total += num
	return total


def average(numbers):
	if len(numbers) == 0:
		return 0
	return sum_numbers(numbers) / len(numbers)


def find_max(numbers):
	if not numbers:
		return None
	m = numbers[0]
	for num in numbers:
		if num > m:
			m = num
	return m


def find_min(numbers):
	if not numbers:
		return None
	m = numbers[0]
	for num in numbers:
		if num < m:
			m = num
	return m


def main():
	try:
		n = int(input("How many numbers? "))
	except ValueError:
		print("Error: please enter an integer.")
		return

	if n <= 0:
		print("Error: number of items must be positive.")
		return

	numbers = []
	for i in range(1, n + 1):
		try:
			v = float(input(f"Enter number {i}: "))
		except ValueError:
			print("Error: please enter a numeric value.")
			return
		numbers.append(v)

	print("\nResults:")
	print(f"Sum:     {sum_numbers(numbers)}")
	print(f"Average: {average(numbers)}")
	print(f"Maximum: {find_max(numbers)}")
	print(f"Minimum: {find_min(numbers)}")


if __name__ == "__main__":
	main()

