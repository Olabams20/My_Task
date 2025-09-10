# Task4: Tuple Unpacking
name = input("what's your fist name? ")
age = input("what's your age ")
favorite_color = input("what's your favorite colour ")
home_town = input("what's your home town name ")
user_details = (name, age, favorite_color, home_town)
name, age, favorite_color, home_town = user_details
print(f"Name: {name}\nAge: {age}\nFavorite color: {favorite_color}\nHome town: {home_town}")
