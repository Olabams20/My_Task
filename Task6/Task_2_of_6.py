# Task2: Unique Name Collector
names = set()
num_names = int(input("How many names: "))
for _ in range(num_names):
    name = input("Enter a name: ")
    names.add(name)
print("Names in alphabetical order:")
print(sorted(names))