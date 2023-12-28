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
# print(student_scores[key])

for key in student_scores:
  if student_scores[key] >= 91:
    student_scores[key] = 'Outstanding'
  elif student_scores[key] >= 81:
    student_scores[key] = 'Exceeds Expectations'
  elif student_scores[key] >= 71:
    student_scores[key] = 'Acceptable'
  else: student_scores[key] = 'Fail'

  student_grades = student_scores

# 🚨 Don't change the code below 👇
print(student_grades)

# Nesting Dictionary in a Dictionary
travel_log = {
  "France": {"cities_visited": ["Paris", "Lille","Dijon"], "total_visits": 21},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 6},
}
print(travel_log)
# Nesting Dictionary in a List

travel_log = [
  {
    "country":"France",
    "cities_visited": ["Paris", "Lille","Dijon"],
    "total_visits": 21},
  {
    "country":"Germany",
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 6},
]
print(travel_log)

