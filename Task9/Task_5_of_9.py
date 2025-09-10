# Task6: Breakdown of the Admission Process

# Input test score
score = int(input("What's your test score? "))

# Check if UNILAG was chosen
unilag_choice = input("Did you choose UNILAG? (yes/no) ").lower() == 'yes'

# Check if O'level grades are good
o_level_grades = input("Do you have good O'level grades? (yes/no) ").lower() == 'yes'

# Check if the candidate participated in Post-UTME
post_utme = input("Did you participate in Post-UTME? (yes/no) ").lower() == 'yes'

# Admission decision using if-else
if score >= 200 and unilag_choice and o_level_grades and post_utme:
    admitted = True
    message = "Congratulations! You're in"
else:
    admitted = False
    message = "Sorry, try again next time!"

# Output the results
print("Admitted:", admitted)
print("Message:", message)
