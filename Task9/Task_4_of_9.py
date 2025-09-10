def simulated_ussd_menu_interaction ():
    print("Welcome to our mobile service!")
    ussd_code = input("Dial Ussd code (7209): ")

    if ussd_code == "7209":
        print("\nMenu:")
        print("1. Check balance")
        print("2. Buy Airtime")
        print("3. Buy Data")

        option = int(input("Enter your choice: "))

        if option == 1:
            print("Your balance is: #50,000")
        elif option == 2:
            amount = float(input("Enter amount to buy airtime: ")) 
            print(f"Confirmation: You have bought airtime worth #{amount:.2f}")
        elif option == 3:
            amount = float(input("Enter amount to buy data: "))
            print(f"Confirmation: You have bought data worth #{amount:.2f}")
        else:
            print("Invalide option")
        print("Transaction summary: Successful")
simulated_ussd_menu_interaction()