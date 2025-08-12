# Write a program to take a string input from the user and display it in uppercase.
first_name = input("Enter your first name:")
last_name = input("Enter your last name:")
print(first_name.upper() + "" + last_name.upper())

# Given the string "python", print its first and last characters.
word = "python"
print("First character:", word[0::5])

# Ask the user for their name and print "Hello, <name>!" where <name> is the user’s input.
name = input ("what is your name?")
print(f"Hello! My name is {name}!")

# Write a program to count the number of characters in a string without using len().
text = "Olabams"
print(sum(1 for _ in text))
# Given "Hello World", replace "World" with "Python".
text = "Hello world"
print(text.replace("world", "python"))

