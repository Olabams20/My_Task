# Task4: Create a Unique Voters Registration System
voters_name = set()
num_voters = int(input("How many voters: "))
for _ in range(num_voters):
    voter = input("Enter a name: ")
    if voter in voter:
        print("Already registered!") 
    else:
        voters.add(voter) 
print("unique voters:", len(voter), "voters!")
