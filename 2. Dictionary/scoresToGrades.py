# created a dictonary  student_scores in which key is student name and value is score
# convery their scores to grade in a new dictonary student_grades

student_scores = {
    "Red": 99,
    "Yellow": 52,
    "Green": 87,
    "Blue": 33,
    "White": 66,
}


def getGrades(score):
    if score > 90:
        return "Outstanding"
    elif score > 80 and score <= 90:
        return "Excellent"
    elif score > 65 and score <= 80:
        return "Good"
    elif score > 50 and score <= 65:
        return "Needs Improvement"
    elif score <= 50:
        return "Fail"


student_grades = {}
for i in student_scores:
    student_grades[i] = getGrades(student_scores[i])

print(student_grades)
