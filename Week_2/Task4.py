# Task4: Unique Members Registration
user_input = input("Enter three names seperated by commas: ")
names = set(user_input.split(","))
names = {name.strip(): len(name.strip()) for name in names}
print(names)