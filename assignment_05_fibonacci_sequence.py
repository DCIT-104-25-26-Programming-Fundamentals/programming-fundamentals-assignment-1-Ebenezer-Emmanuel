# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
#
# The Fibonacci sequence is a series of numbers where each number is the sum
# of the two numbers before it:
#
#   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# Write a Python program with TWO parts, each implemented as a function.
#
# -----------------------------------------------------------------------------
# PART A — Print the First N Terms
# -----------------------------------------------------------------------------
# - Ask the user how many terms (N) to display.
# - Print the first N numbers of the Fibonacci sequence on one line.
#
# Example:
#   How many terms? 7
#   Fibonacci sequence: 0 1 1 2 3 5 8
#
# -----------------------------------------------------------------------------
# PART B — Check if a Number Belongs to the Sequence
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Determine whether that number is a Fibonacci number.
# - Print an appropriate message.
#
# Example:
#   Enter a number to check: 13
#   13 is a Fibonacci number.
#
#   Enter a number to check: 20
#   20 is NOT a Fibonacci number.
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use a loop (not recursion) to generate the sequence in both parts.
# - N must be a positive integer. If it is not, print an error message.
# - Each part must be implemented in its own function (see scaffold below).
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def generate_fibonacci(n):
    """Generates and prints the first N terms of the Fibonacci sequence."""
    if n <= 0:
        print("Please enter a positive integer greater than 0.")
        return

    fib_sequence = []
    a, b = 0, 1
    
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b

    # Convert the numbers to strings to join them nicely with spaces
    print("Fibonacci sequence:", " ".join(map(str, fib_sequence)))


def check_fibonacci(target):
    """Checks whether a given number is part of the Fibonacci sequence."""
    if target < 0:
        print(f"{target} is NOT a Fibonacci number.")
        return

    a, b = 0, 1
    
    # Generate numbers using a loop until we reach or exceed the target
    while a < target:
        a, b = b, a + b

    if a == target:
        print(f"{target} is a Fibonacci number.")
    else:
        print(f"{target} is NOT a Fibonacci number.")


# --- Main Program Runner ---
if __name__ == "__main__":
    # Part A
    try:
        n_terms = int(input("How many terms? "))
        generate_fibonacci(n_terms)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

    print() # blank line for formatting

    # Part B
    try:
        num_to_check = int(input("Enter a number to check: "))
        check_fibonacci(num_to_check)
    except ValueError:
        print("Invalid input! Please enter a valid integer.")S