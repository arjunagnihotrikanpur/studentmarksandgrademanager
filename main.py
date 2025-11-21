import inputMarks
import processing
import report
import storage

def displayOptions():
    
    print("\n")
    print("CHOOSE AN OPTION: ")
    print("1. Add Student")
    print("2. View Student")

    print("\n")
    option = int(input("Enter Option (1-2): "))
    print("\n")
    return option

def start():
    print("\n\n\n")
    print("***********************************************")
    print("Welcome to Student Marks & Grade System")
    print("***********************************************")
    choice = displayOptions()
    print("\n\n\n")

    if (choice == 1):
        rollno, marks = inputMarks.inputMarksFromUser()
        total, perc, grades = processing.calculate(marks)
        report.showReport(marks, grades, total, perc)
        storage.storeInformation(rollno, marks, grades, total, perc)
        print("\n\n")
    elif (choice == 2):
        roll = input("Enter student roll number to search: ")

        student = storage.searchStudent(roll)

        if student:
            marks = student["marks"]
            grades = student["grades"]
            total = student["total"]
            perc = student["percentage"]

            report.showReport(marks, grades, total, perc)
    elif (choice == 3):
        pass

start()