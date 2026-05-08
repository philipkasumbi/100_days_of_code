student_scores = {
    "paul": 79,
    "james": 86,
    "ken": 94,
    "mark": 61,
    "bumpy": 57,
    "johnson": 87
}
student_grades = {}
for key in student_scores:
    if student_scores[key] > 89:
        student_grades[key] = "Outstanding"
    elif student_scores[key] > 79:
        student_grades[key] = "Exceeds Expectation"
    elif student_scores[key] > 69:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "fail"

print(student_grades)
