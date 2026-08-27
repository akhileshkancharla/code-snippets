"""
Python Recursion Examples and Code Snippets
"""

# 1. Factorial
def factorial(n: int) -> int:
    """Calculate factorial of n using recursion."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("--- Factorial ---")
print(f"Factorial of 5: {factorial(5)}")


# 2. Fibonacci Sequence (nth number)
def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number."""
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print("\n--- Fibonacci ---")
print(f"Fibonacci(7): {fibonacci(7)}")


# 3. Sum of Array/List Elements
def sum_array(arr: list) -> int:
    """Sum elements of a list recursively."""
    if not arr:
        return 0
    return arr[0] + sum_array(arr[1:])

print("\n--- Sum of List Elements ---")
numbers = [1, 2, 3, 4, 5]
print(f"Sum of {numbers}: {sum_array(numbers)}")


# 4. String Reversal
def reverse_string(s: str) -> str:
    """Reverse a string recursively."""
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

print("\n--- String Reversal ---")
text = "hello"
print(f"Reverse of '{text}': {reverse_string(text)}")


# 5. Sum of Digits
def sum_of_digits(n: int) -> int:
    """Calculate the sum of digits of a number."""
    if n == 0:
        return 0
    return (n % 10) + sum_of_digits(n // 10)

print("\n--- Sum of Digits ---")
num = 12345
print(f"Sum of digits of {num}: {sum_of_digits(num)}")


# 6. Tower of Hanoi
def tower_of_hanoi(n: int, source: str, destination: str, auxiliary: str):
    """Solve Tower of Hanoi puzzle."""
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, destination, source)

print("\n--- Tower of Hanoi (3 disks) ---")
tower_of_hanoi(3, 'A', 'C', 'B')
