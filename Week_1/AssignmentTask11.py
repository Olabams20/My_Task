def nigerian_currency_converter ():
    amount_in_naira =float(input("Enter amount in naira: "))
    exchange_rate_ussd = float(input("Enter exchange rate to us dollars: "))
    exchange_rate_gbp = float(input("Enter exchange rate to british pounds: "))

    amount_in_usd = amount_in_naira / exchange_rate_ussd
    amount_in_gbp = amount_in_naira / exchange_rate_gbp
    print(f"Currency conversion for {amount_in_naira:,.2f} NGN:")
    print(f"Usd: {amount_in_usd:,.2f} $")
    print(f"Gbp: {amount_in_gbp:,.2f}€")
    
nigerian_currency_converter()