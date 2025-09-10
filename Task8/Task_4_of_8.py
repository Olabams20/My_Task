# Task4: Student Record
student = {}
name = input("What's the Student's name? ")
age = int(input("How old is the student? "))
student['name'] = name
student['age'] = age
student['scores'] = [70, 85, 90]
average_score = sum(student['scores']) / len(student['scores'])
student['passed'] = average_score >= 50
student['teenager'] = 13 <= student['age'] <= 19
print(f"Name: {student['name']}\nAge: {student['age']}\nScores: {student['scores']}\nPassed: {student['passed']}\nTeenager: {student['teenager']}")