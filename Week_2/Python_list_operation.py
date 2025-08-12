# Concatenation (+)
list1 = [20, 30, 40]
list2 = [50, 60, 70]
result = list1 + list2
print(result)  # [20, 30, 40, 50, 60, 70] 

# Repetition (*)
nums = [4, 5, 6]
repeated = nums * 3
print(repeated)  # [4, 5, 6, 4, 5, 6, 4, 5, 6]

# Indexing
fruits = ["apple", "banana", "cherry", "mango"]
print(fruits[0])   # apple
print(fruits[-1])  # mango(negative index starts from the end)

# Slicing
numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])   # [1, 2, 3]
print(numbers[:3])    # [0, 1, 2]
print(numbers[3:])    # [3, 4, 5]
print(numbers[::2])   # [0, 2, 4] (step of 2)

# Membership (in/not in)
colors = ["red", "green", "blue"]
print("green" in colors)   # True
print("yellow" not in colors)  # True

# Length (len())
items = ["pen", "book", "laptop"]
print(len(items))  # 3

# Min and Max (min() / max())
nums = [5, 2, 9, 1]
print(min(nums))  # 1
print(max(nums))  # 9

# Sum (sum())
numbers = [1, 2, 3, 4]
print(sum(numbers))  # 10

# List Comprehension
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# Copying a List
a = [1, 2, 3]
b = a.copy()  # or b = list(a)
print(b)  # [1, 2, 3]