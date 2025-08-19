# Task2: Comment the code below appropriately, and using doctring, explain what the code is doing.
name = input("Enter your name: ")
citizenship = input("Are you a Nigerian citizen? (yes/no): ")
is_nigerian = citizenship.lower() == "yes"
enrollment = input("Are you a full-time undergraduate student in a Nigerian university? (yes/no): ")
is_undergraduate = enrollment.lower() == "yes"
other_scholarships = input("Do you have any other scholarships from the Oil and Gas industry? (yes/no): ")
has_other_scholarships = other_scholarships.lower() == "yes"
distinctions = int(input("How many distinctions (As and Bs) do you have in your WAEC/NECO exams? "))
eligibility = is_nigerian and is_undergraduate and (not has_other_scholarships) and (distinctions >= 5)
print(f"Candidate: {name}\nEligible: {eligibility}")