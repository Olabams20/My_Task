# Upper()
name = "Ada Balogun"
print(name.upper ()) # ADA BALOGUN
print(name.lower()) # ada balogun
print(name.title()) # Ada Balogun 
print(name.capitalize()) # Ada Balogun


# lower
sentence = "python is amazing"
print(sentence.lower())

# string()
text = "Abuja"
print(text.strip())

# replace()
message = "I love Java"
print(message.replace("Java", "python"))

# swapcase()
text = "Hello ABEOKUTA"
print(text.swapcase())

# lstrip()
text  = "Nigeria"
print(text.lstrip())

# rstrip()
text = "Nigeria  "
print(text.rstrip())

# split
fruits = "mango orange banana"
print(fruits.split())

# rsplit()
text = "one,two,three,four"
print(text.rsplit(",", 2))

# splitlines()
lines = "Line 1\nLine 2\nLine 3"
print(lines.splitlines())  

# join()
words = ["I", "love", "Python"]
print(" ".join(words))  

# center()
text = "Python"
print(text.center(20, "-")) 

# ljust()
text = "Python"
print(text.ljust(10, "*")) 

# rjust()
text = "Python"
print(text.rjust(10, "*"))  

# zfill()
num = "42"
print(num.zfill(5)) 

# isalpha()
print("Lagos".isalpha())  # True
print("Lagos123".isalpha())  # False

# isdigit()
print("12345".isdigit())  # True
print("123a".isdigit())   # False

# isalnum()
print("Python3".isalnum())  # True
print("Python 3".isalnum()) # False

# isspace()
print(" ".isspace()) # True
print("My Love". isspace()) # False

# islower()
print("My name".islower())   # False
print("my name".islower())   # True

# isupper()
print("PYTHON".isupper())    # True
print("python".isupper())    # False
print("python".isupper())    # False

# istitle()
print("The Car is Moving".istitle())     # False
print("The car is moving".istitle())     # False
print("The Car Is Moving".istitle())     # True
print("THE CAR IS MOVING".istitle())     # False
print("the car is moving".istitle())     # False