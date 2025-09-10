# Import functions from your package
from file_ops import save_participant, load_participants
from pathlib import Path

# Define where the CSV file will be saved
data_file = Path("participants.csv")

def get_participant_details():
    """
    Prompt user for participant details and return as a dictionary.
    """
    name = input("Enter participant's name: ")
    age = int(input("Enter participant's age: "))
    phone = input("Enter participant's phone number: ")
    track = input("Enter participant's track: ")
    
    return {"name": name, "age": age, "phone": phone, "track": track}

# Main menu loop
while True:
    print("\n=== Contact Saver Menu ===")
    print("1. Add participant")
    print("2. View all participants")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        participant = get_participant_details()
        save_participant(data_file, participant)
        print(":white_tick: Participant saved successfully!")

    elif choice == "2":
        display_participants()

    elif choice == "3":
        print(": Exiting program. Goodbye!")
        break

    else:
        print(": Invalid choice. Please enter 1, 2, or 3.")
















