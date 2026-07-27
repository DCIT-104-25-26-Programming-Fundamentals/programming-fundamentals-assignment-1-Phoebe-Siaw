# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
def transpose(matrix):
	if not matrix:
		return []
	rows = len(matrix)
	cols = len(matrix[0])
	result = [[matrix[r][c] for r in range(rows)] for c in range(cols)]
	return result


def add_matrices(a, b):
	rows = len(a)
	cols = len(a[0])
	res = [[0] * cols for _ in range(rows)]
	for i in range(rows):
		for j in range(cols):
			res[i][j] = a[i][j] + b[i][j]
	return res


def multiply_matrices(a, b):
	m = len(a)
	n = len(a[0])
	p = len(b[0])
	res = [[0] * p for _ in range(m)]
	for i in range(m):
		for j in range(p):
			s = 0
			for k in range(n):
				s += a[i][k] * b[k][j]
			res[i][j] = s
	return res


def read_matrix(rows, cols):
	matrix = []
	for r in range(1, rows + 1):
		while True:
			line = input(f"Enter row {r}: ").strip()
			parts = line.split()
			if len(parts) != cols:
				print(f"Error: expected {cols} values.")
				continue
			try:
				row = [float(x) for x in parts]
			except ValueError:
				print("Error: please enter numeric values.")
				continue
			matrix.append(row)
			break
	return matrix


def print_matrix(mat):
	for row in mat:
		print(" ".join(str(int(x)) if x.is_integer() else str(x) for x in row))


def main():
	print("Choose operation:\n1) Transpose\n2) Add matrices\n3) Multiply matrices")
	choice = input("Enter choice (1-3): ").strip()
	if choice == '1':
		try:
			r = int(input("Enter number of rows: "))
			c = int(input("Enter number of columns: "))
		except ValueError:
			print("Error: invalid size")
			return
		mat = read_matrix(r, c)
		print("Transposed Matrix:")
		print_matrix(transpose(mat))
	elif choice == '2':
		try:
			r = int(input("Enter number of rows: "))
			c = int(input("Enter number of columns: "))
		except ValueError:
			print("Error: invalid size")
			return
		print("Matrix A:")
		a = read_matrix(r, c)
		print("Matrix B:")
		b = read_matrix(r, c)
		print("Sum:")
		print_matrix(add_matrices(a, b))
	elif choice == '3':
		try:
			m = int(input("Enter number of rows for A: "))
			n = int(input("Enter number of columns for A (and rows for B): "))
			p = int(input("Enter number of columns for B: "))
		except ValueError:
			print("Error: invalid size")
			return
		print("Matrix A:")
		a = read_matrix(m, n)
		print("Matrix B:")
		b = read_matrix(n, p)
		print("Product A x B:")
		print_matrix(multiply_matrices(a, b))
	else:
		print("Invalid choice")


if __name__ == "__main__":
	main()

