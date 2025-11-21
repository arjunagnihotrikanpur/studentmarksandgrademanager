import json
import os

def storeInformation(roll_number, marks, grades, total, percentage, filename="students.json"):

    # If file exists, load it; otherwise create empty structure
    if os.path.exists(filename):
        with open(filename, "r") as file:
            data = json.load(file)
    else:
        data = {"students": {}}

    # Add/update student data
    data["students"][roll_number] = {
        "marks": marks,
        "grades": grades,
        "total": total,
        "percentage": percentage
    }

    # Save back to file
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Student {roll_number} stored successfully!")

def searchStudent(roll_number, filename="students.json"):
    # If file doesn't exist
    if not os.path.exists(filename):
        print("No student data file found!")
        return None

    # Load data
    with open(filename, "r") as file:
        data = json.load(file)

    # If no students stored yet
    if "students" not in data or len(data["students"]) == 0:
        print("No student records found!")
        return None

    # Check if roll number exists
    if roll_number not in data["students"]:
        print(f"No student found with roll number {roll_number}")
        return None

    # Return the student data
    return data["students"][roll_number]