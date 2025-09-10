# School fees breakdown
def school_fees_breakdown ():
    school_name = input("Enter school name: ")
    tuition_fee = float(input("Enter tuition fee: #"))
    hostel_fee = float(input("Enter hostel fee: #"))
    feeding_fee = float(input("Enter feeding fee: "))

    total_fee = tuition_fee + hostel_fee + feeding_fee

    print(f"\nreceipt for De-grains school:")
    print(f"Tuition fee: #Tuition_fee:250,000.00")
    print(f"Hostel fee: #{hostel_fee:,.2f}")
    print(f"Feeding fee: #{feeding_fee:,.2f}")
    print(f"Total fee: #{total_fee:,.2f}")
school_fees_breakdown ()    