# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
#
# Write a Python program that generates multiplication tables using loops
# and functions.
#
# -----------------------------------------------------------------------------
# PART A — Single Table
# -----------------------------------------------------------------------------
# - Ask the user to enter a number.
# - Print the multiplication table for that number from 1 to 12.
#
# Expected output (if user enters 5):
#
#   Multiplication Table for 5:
#   5  x  1  =  5
#   5  x  2  =  10
#   5  x  3  =  15
#   ...
#   5  x  12 =  60
#
# -----------------------------------------------------------------------------
# PART B — Bonus: Tables from 1 to N
# -----------------------------------------------------------------------------
# - Ask the user to enter a number N.
# - Print the full multiplication table for every number from 1 to N.
# - Add a separator line (e.g. "---") between each table.
#
# Expected output (if user enters 3):
#
#   Multiplication Table for 1:
#   1  x  1  =  1
#   ...
#   1  x  12 =  12
#   ---------------------------
#   Multiplication Table for 2:
#   2  x  1  =  2
#   ...
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - N must be a positive integer. If the user enters an invalid value,
#   print an error message and stop.
# - Each part must be in its own function (see scaffold below).
# - Complete Part A before attempting Part B.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def print_single_table(num):
    """Prints the multiplication table for a single number from 1 to 12."""
    print(f"\nMultiplication Table for {num}:")
    for i in range(1, 13):
        # :2d formats the multiplier so 1-9 align nicely with 10-12
        print(f"  {num}  x  {i:2d}  =  {num * i}")


def print_tables_up_to_n(n):
    """Prints multiplication tables for all numbers from 1 up to N."""
    for current_num in range(1, n + 1):
        print_single_table(current_num)
        # Add a separator line after every table except the last one
        if current_num < n:
            print("  ---------------------------")


# --- Main Program ---
if __name__ == "__main__":
    # Part A Execution
    try:
        user_num = int(input("Enter a number for Part A: "))
        if user_num <= 0:
            print("Error: Please enter a positive integer.")
        else:
            print_single_table(user_num)
    except ValueError:
        print("Error: Invalid input! Please enter a valid whole number.")

    print("\n" + "=" * 40 + "\n")

    # Part B Execution
    try:
        max_n = int(input("Enter a number N for Part B (1 to N): "))
        if max_n <= 0:
            print("Error: N must be a positive integer.")
        else:
            print_tables_up_to_n(max_n)
    except ValueError:
        print("Error: Invalid input! Please enter a valid whole number.")