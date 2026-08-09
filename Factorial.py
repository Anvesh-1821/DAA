import time

# Iterative Factorial
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Recursive Factorial
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

# Main program
n = int(input("Enter a non-negative integer (e.g., 20): "))

if n < 0:
    print("Invalid input! Please enter a non-negative integer.")
else:
    # Measure Iterative Time
    start = time.perf_counter_ns()
    result_iterative = factorial_iterative(n)
    end = time.perf_counter_ns()

    iterative_time = end - start

    # Measure Recursive Time
    start = time.perf_counter_ns()
    result_recursive = factorial_recursive(n)
    end = time.perf_counter_ns()

    recursive_time = end - start

    # Display Results
    print(f"\n--- Results for {n}! ---")
    print("Iterative Result :", result_iterative)
    print("Iterative Time   :", iterative_time, "ns")

    print("-------------------------------")

    print("Recursive Result :", result_recursive)
    print("Recursive Time   :", recursive_time, "ns")
