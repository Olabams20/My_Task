voters_name = set()

try:
    num_voters = int(input("How many voters: "))
    for _ in range(num_voters):
        voter = input("Enter a name: ")
        if voter in voters_name:
            print("Already registered!")
        else:
            voters_name.add(voter)
except ValueError:
    print("Invalid input! Please enter a valid number for the number of voters.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Unique voters:", len(voters_name), "voters!")
