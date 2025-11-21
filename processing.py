def calculate(marks):
    total = 0
    grades = []

    for subject, mark in marks.items():
        print(f"{subject}: {mark}")
        total += mark

    for subject, mark in marks.items():
        if 90 <= mark <= 100:
            grade = "A"
        elif 80 <= mark < 90:
            grade = "B"
        elif 70 <= mark < 80:
            grade = "C"
        elif 60 <= mark < 70:
            grade = "D"
        else:
            grade = "F"

        grades.append(grade)

    # Assuming 5 subjects → total out of 500  
    perc = (total / 500) * 100  

    return total, perc, grades
