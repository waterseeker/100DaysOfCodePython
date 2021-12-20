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
    if value > 90:
        grade = "Outstanding"
    elif value > 80:
        grade = "Exceeds Expectations"
    elif value > 70:
        grade = "Acceptable"
    else:
        grade = "Fail"
    student_grades[key] = grade

# 🚨 Don't change the code below 👇
print(student_grades)
