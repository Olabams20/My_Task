# Single quotes
name = 'Ade'
print(f"my name is Ade.")

# Double quotes
greeting = "Hello"
print(f"greeetings, Ade tell me a story.")

# Triple quotes (for multi-line strings)
story = '''Once upon a time,
there was a coder named Ade.'''
print(f"{story}")

# String with numbers and symbols
password = "p@ssw0rd123"
print(f"My password is: {password}")

# Indexing
word = "Python"
print(word[0])  # P
print(word[1]) # y
print(word[2]) # t
print(word[3]) # h
print(word[4]) # o
print(word[5]) # n

# Slicing 
word = "Community"
print(word[0:9])   # Community
print(word[4:])    # unity
print(word[:3])    # Com
print(word[::4])   # n
print(word[::7])

# String Concatenation & repetition
# Concatenation
a = "Car"
b = "Park"
print(a + " " + b)  # Car Park

# Repetition
word = "OMG! "
print(word * 3)  # OMG! OMG! OMG!

# String searching & cheacking
# Membership
text = "Python programming"
print("Python" in text)   # True
print("Java" not in text) # True

# find() / rfind()
text = "Hello World"
print(text.find("o"))   # 4
print(text.rfind("o"))  # 7

# index() / rindex()
text = "Hello World"
print(text.index("World"))   # 6

# startswith() / endswith()
filename = "data.csv"
print(filename.startswith("data"))  # True
print(filename.endswith(".csv"))    # True