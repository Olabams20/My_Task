# Task1: Your Favorite Life Quote
quote = input("Enter your favorite quote: ")
title_case_quote =quote.title()
print(f"\"{title_case_quote}\"")

# Task 2: Shopping List Manager
shopping_list = [input("Item 1: "), input("Item 2: "), input("Item 3: ")]
print(", ".join(shopping_list))

# Task 3: Word Counter
sentence = input("Enter a sentence: ")
words = sentence.split()
print(f"Number of words: {len(words)}")

# Task 4: Name Organizer
names = input("Enter 5 names: ").split()
print(sorted([n.lower() for n in names]))

# Task 5: Student Score Tracker
name = input("Name:"); 
score = input("score:"),
print("name","score")

# Task 6: Word Analyzer
word = input("word:")
print(len(word), word[::-1])

# Task 7: List Manipulation
city = ["Ikeja", "Ibadan", "Abeokuta", "Akure", "Ilorin" ]; 
city[1] = input("New city: ")
city.pop()
city.insert(0,input ("New city at start: ")) 
print(city)