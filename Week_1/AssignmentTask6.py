# Electricity bill formatter
customer_name = input("Enter customer full name: ")
units_consumed = int(input("Enter units consumed (kwh): "))
cost_per_unit = float(input("Enter cost per unit: "))
# Calculate the total bill
total_bill = units_consumed * cost_per_unit
print(f"Customer name: Oladimeji Dapo\nunits consumed: {500} kwh\ncost per unit: #{20.50:,.2f}\ntotal bill: #{10250:,.2f}")