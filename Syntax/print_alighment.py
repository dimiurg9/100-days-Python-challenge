"""
print(f"{leftAlign : <25}{centerAlign : ^20}{rightAlign : >25}")
"""
students_scores = {
    "John": 60,
    "Bill":81,
    "Ueban":93,
    "Mashish":70,
    "Rohit":90
}
student_grades = {}
print(f"{'student_grades'.upper(): <20} {'Grade'.upper()}")
print()
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

"""
output: 
John                 Fail
Bill                 Exceeds expectations
Ueban                Outstanding
Mashish              Fail
Rohit                Exceeds expectations
"""