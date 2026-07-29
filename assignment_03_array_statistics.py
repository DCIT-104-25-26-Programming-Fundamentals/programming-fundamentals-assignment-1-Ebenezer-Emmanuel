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

# -----------------------------------------------------------------------------
# HELPER FUNCTIONS (Manual Calculations)
# -----------------------------------------------------------------------------

def compute_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

def compute_average(numbers):
    # Total divided by total count of elements
    total = compute_sum(numbers)
    return total / len(numbers)

def compute_maximum(numbers):
    # Assume the first number is the largest to start
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

def compute_minimum(numbers):
    # Assume the first number is the smallest to start
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

def main():
    # Prompt for how many numbers to collect
    n = int(input("How many numbers? "))
    
    # Validation: N must be a positive integer (> 0)
    if n <= 0:
        print("Error: Please enter a positive integer greater than 0.")
        return

    numbers_list = []
    
    for i in range(1, n + 1):
        num = float(input(f"Enter number {i}: "))
        numbers_list.append(num)

    total_sum = compute_sum(numbers_list)
    avg_val = compute_average(numbers_list)
    max_val = compute_maximum(numbers_list)
    min_val = compute_minimum(numbers_list)

    print("\nResults:")
    print(f"Sum:     {total_sum if total_sum % 1 != 0 else int(total_sum)}")
    print(f"Average: {round(avg_val, 2)}")
    print(f"Maximum: {max_val if max_val % 1 != 0 else int(max_val)}")
    print(f"Minimum: {min_val if min_val % 1 != 0 else int(min_val)}")

if __name__ == "__main__":
    main()