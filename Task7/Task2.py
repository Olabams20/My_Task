# Task2: Super Market Price List
item = {
    "Super Market": {
        "Bread": 1200.0,
        "Milk": 500.0,
        "Sugar": 400.0,
        "Apple": 300.0,
        "Tea": 600.0
    }
}

#...

while True:
    item_to_update = input("\nEnter the item to update it's price (or 'exit to stop): ") 
    if item_to_update.lower() == 'exit':
        break
    if item_to_update.capitalize() in item["Super Market"]:
        new_price = float(input(f"Enter new price for {item_to_update.capitalize()}: "))
        item["Super Market"][item_to_update.capitalize()] = new_price
        print(f"{item_to_update.capitalize()} updated to {new_price}")
    else:
        print(f"{'Item to update'} not found.")             