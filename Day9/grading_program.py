student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for key, value in student_scores.items():
    student = key
    if value <= 70:
        grade = "Fail"
    elif value >= 71 and value < 81:
        grade = "Acceptable"
    elif value >= 81 and value < 91:
        grade = "Exceeds Expectations"
    else:
        grade = "Outstanding"
    student_grades[student] = grade


# 🚨 Don't change the code below 👇
print(student_grades)
