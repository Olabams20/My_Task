# Python operators
# 1. Comparison Operators
# Comparison operators are used to compare two values. The result is always True or False, Yes or No, 0 and 1.

a = 10
b = 20
# Equal to
print(a == b)                         # Output is False
# Not equal to           
print(a != b)                          # Output is True
# Greater than 
print(a > b)                           # Output is False
# Less than  
print(a < b)                           # Output is True
# Greater than or equal to 
print(a >= 10)                         # Output is True
# Less than or equal to 
print(b <= 25)                         # Output is True

# Use case Example- Student Exam Result
score = 75
print(score >= 50)  # True (Passed)
print(score < 50)   # False (Failed)
print(score == 100) # False (Not full marks)


# 2. Assignment Opertaors
x = 10           # Assigns value 10 to x (means x = 10)   
print("Initial value:", x)        # Output: Initial value: 10

x += 5           # Adds 5 to x (x = x + 5) i.e 10 + 5 = 15 
print("After x += 5:", x)          

x -= 2      # Subtracts 2 from x. i.e 15 - 2 = 13
print("After x -= 2:", x)

x *= 3      # Multiplies x by 3. i.e 13 * 3 = 39
print("After x *= 3:", x)

x /= 4        #  Divides x by 4. i.e 39 divided by 4 = 9.75    
print("After x /= 4:", x)

x %= 3        # Stores remainder after division 
print("After x %= 3:", x)

x = 4
x **= 2      # Raises x to the power of 2 
print("After x **= 2:", x)

x //= 3    #  Floor divides x by 2. i.e 16 divided by 5 (does not include the remainder after the division)
print("After x //= 3:", x)

# Use case Example:

# Define variables
balance = 1000
deposit = 200
withdraw = 150
balance += deposit   # Add deposit
balance -= withdraw  # Subtract withdrawal
print("Updated Balance:", balance)  
# Output: Updated Balance: 1050


# 3. Logical Operators
x = 10
y = 20
# and operator      (True if both conditions are true)
print(x > 5 and y > 15)  # True

# or operator         (True if at least one condition is true)
print(x < 5 or y > 15)   # True

# not operator          (True if the condition is false)
print(not(x == 10))      # False

# Use case example1 - Scholarship Eligibility

#Define variables
age = 17
score = 85

# Must be younger than 18 AND score above 80
eligible = (age < 18) and (score > 80)

print("Scholarship Eligible:", eligible)  
# Output: Scholarship Eligible: True

# Use case example2 - Event Access
age = 22
has_ticket = False

can_enter = (age >= 18) and (has_ticket or age < 25)

print("Access Granted:", can_enter)  
# Output: Access Granted: True (because age < 25 even without ticket)


