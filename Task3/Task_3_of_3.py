# Ask the user for a sentence and print each word on a new line.
sentence = input("Enter a sentence:")
words = sentence.split()
for word in words:
    print(word)

# Replace all spaces in a string with underscores (_).
string = "Good Boy"
new_string = string.replace('', '_')
print(new_string)

#  Count how many times the letter "a" appears in "Banana".
fruit = "Banana"
count_a = fruit.lower().count('a')
print(count_a)

# Check if a given string starts with "https://".
url = input("Enter a URL: ")
if url.startswith('https://'):
    print("The URL start with https://")
else:
    print("The URL does not start with https://")
