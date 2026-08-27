"""
Python Loops Examples and Code Snippets
"""

# 1. For Loop with range
print("--- For Loop (range) ---")
for i in range(1, 6):
    print(f"Count: {i}")

# 2. Iterating over a List
print("\n--- Iterating over a List ---")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")

# 3. Iterating with enumerate()
print("\n--- Iterating with Enumerate ---")
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")

# 4. Iterating over a Dictionary
print("\n--- Iterating over a Dictionary ---")
user = {"name": "Alice", "role": "Developer", "language": "Python"}
for key, value in user.items():
    print(f"{key}: {value}")

# 5. While Loop
print("\n--- While Loop ---")
count = 5
while count > 0:
    print(f"Countdown: {count}")
    count -= 1
print("Liftoff!")

# 6. Break and Continue
print("\n--- Break and Continue ---")
for num in range(1, 10):
    if num == 3:
        continue  # Skip 3
    if num == 7:
        break     # Stop at 7
    print(f"Number: {num}")

# 7. Nested Loops
print("\n--- Nested Loops ---")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})", end=" ")
    print()

# 8. List Comprehension (Loop shorthand)
print("\n--- List Comprehension ---")
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")
