# Task5: Modify Tuple Indirectly
shopping = tuple([input("Item 1: "), input("Item 2: "), input("Item 3: ")])
shopping = list(shopping)
shopping = shopping + [input("Add item 4: "), input("Add item 5: ")]
shopping = tuple(shopping)
print(" |".join(shopping))