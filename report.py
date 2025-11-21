def showReport(marks, grades, total, percentage):
    subjects = list(marks.keys())
    
    print("\n-------------------- REPORT CARD --------------------\n")
    print(f"{'Subject':<15}{'Marks':<10}{'Grade'}")
    print("-" * 40)
    
    for i, subject in enumerate(subjects):
        mark = marks[subject]
        grade = grades[i]
        print(f"{subject:<15}{mark:<10}{grade}")
    
    print("\n" + "-" * 40)
    print(f"TOTAL: {total}")
    print(f"PERCENTAGE: {percentage}%")
