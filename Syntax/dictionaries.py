"""
List of students with score to convert into grades
91+ = outstanding
81-90 = exceeds expectation
71-80 = acceptable
70 and less = fail
"""
students_scores = {
    "John": 60,
    "Bill":81,
    "Ueban":93,
    "Mashish":70,
    "Rohit":90
}
student_grades = {}
for key, value in students_scores.items():
    if value >= 91:
        student_grades[key] = "Outstanding"
    elif value >= 81 and value <=90:
        student_grades[key] = "Exceeds expectations"
    elif value >= 71 and value <=80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

for key, value in student_grades.items():
    print(f"{key: <20} {value}")
