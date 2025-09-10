# Task3: Online Store Cart Calculation
items = ["Book", "Pen", "Bag"]
prices = {'Book': 500, 'Pen': 100, 'Bag': 2000}
cart_total = 0
for item in items:
    cart_total += prices[item]
print(f"items: {items}")
print(f"Total Price: #{cart_total}")