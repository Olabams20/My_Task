import csv
from pathlib import Path

def save_participant(path, participant_dict):
    """
    Save a participant's details into a CSV file.
path: Path to the CSV file
participant_dict: dict with participant details, e.g.
      {"name": "Olabams", "age": 25, "phone": "09035487209"}
"""
    path = Path(path)

    # Check if file exists (to know whether to write headers)
    file_exists = path.exists()

    with path.open(mode="a", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=participant_dict.keys())

        # Write header if file is new
        if not file_exists:
            writer.writeheader()

        # Write participant data
        writer.writerow(participant_dict)

def load_participants(path):
    """
    Load all participants from a CSV file.
path: Path to the CSV file
returns: list of dictionaries with participant details
    """
    path = Path(path)

    if not path.exists():
        return []  # No file yet, return empty list

    with path.open(mode="r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)








