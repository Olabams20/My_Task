# Task1:  Create and Display
dishes = tuple(input("Enter dish:") for _ in range(3))
print(", ".join(dishes))
print("\n".join(dishes))

# Task2: Tuple and Input
friends = tuple(input("Enter name:") for _ in range (5))
print(friends[::-1])

# Task3: Tuple Operations
nigerian_states = tuple(input("Enter state:") for _ in range(5))
print("first:", nigerian_states[0], "Last:", nigerian_states[-1])
print("Lagos?", "Yes" if "Lagos" in nigerian_states else "No")
print("count:", len(nigerian_states))

# Task4: Tuple Unpacking
name = input("what's your fist name? ")
age = input("what's your age ")
favorite_color = input("what's your favorite colour ")
home_town = input("what's your home town name ")
user_details = (name, age, favorite_color, home_town)
name, age, favorite_color, home_town = user_details
print(f"Name: {name}\nAge: {age}\nFavorite color: {favorite_color}\nHome town: {home_town}")

# Task5: Modify Tuple Indirectly
shopping = tuple([input("Item 1: "), input("Item 2: "), input("Item 3: ")])
shopping = list(shopping)
shopping = shopping + [input("Add item 4: "), input("Add item 5: ")]
shopping = tuple(shopping)
print(" |".join(shopping))

# Task6: Attendance Tracker
days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
months =  ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug","Sep", "Oct", "Nov", "Dec")
print("Answers:")
name = input("Name? ")
gender = input("Gender? ")
course_track = input("course track? ")
print(f"Name: {name}")
print(f"Gender: {gender}")
print(f"Course track: {course_track}")
print(f"Month: {months}")
print(f"Day: {days}")