# Method 1: Using square brackets
empty_list = []
print(empty_list)    # Output: []

# Method 2: Using the list() constructor
empty_list2 = list()
print(empty_list2)   # Output: []

# List of integers
numbers = [1, 2, 3, 4, 5]
print(numbers)       # Output: [1, 2, 3, 4, 5]

# List of strings
fruits = ["apple", "banana", "cherry"]
print(fruits)        # Output: ['apple', 'banana', 'cherry']

# Mixed data types
mixed_list = ["Alice", 25, 5.8, True]
print(mixed_list)    # Output: ['Alice', 25, 5.8, True]

# From a string (each character becomes an element)
chars = list("hello")
print(chars)         # Output: ['h', 'e', 'l', 'l', 'o']

# Squares of numbers 0–4
squares = [x**2 for x in range(5)]
print(squares)       # Output: [0, 1, 4, 9, 16]

# Even numbers between 0–10
evens = [x for x in range(11) if x % 2 == 0]
print(evens)         # Output: [0, 2, 4, 6, 8, 10]

# Matrix-like list
matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix)        # Output: [[1, 2], [3, 4], [5, 6]]

# Accessing elements in a nested list
print(matrix[0])     # Output: [1, 2]
print(matrix[0][1])  # Output: 2

# Ordered Collection
fruits = ["mango", "orange", "banana"]
print(fruits)        # ['mango', 'orange', 'banana']
print(fruits[0])     # mango (first element)
print(fruits[2])     # banana (third element)

# Allows Duplicates
items = ["rice", "beans", "yam", "rice"]
print(items)         # ['rice', 'beans', 'yam', 'rice']

# Mutable (Can Be Changed)
numbers = [1, 2, 3]
numbers[1] = 20      # Changing element at index 1
print(numbers)       # [1, 20, 3]

#  Can Contain Different Data Types
mixed = [10, "Nigeria", 3.14, True]
print(mixed)         # [10, 'Nigeria', 3.14, True]

#  Can Be Nested
nested_list = [[1, 2], ["a", "b"]]
print(nested_list)       # [[1, 2], ['a', 'b']]
print(nested_list[0][1]) # 2

# Dynamic Size
names = ["Ada"]
names.append("Bola")
names.append("Chidi")
print(names)           # ['Ada', 'Bola', 'Chidi']
