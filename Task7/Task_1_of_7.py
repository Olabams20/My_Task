# ask1: Student Bio Data Storage
def collect_student_data():
    name = input("Enter student's full name: ")
    age = input("Enter student's age: ")
    gender = input("Enter gender (Male/Female): ")
    num_courses = int(input("Enter the number of courses: "))
    courses =[]
    for i in range(num_courses):
        course = input(f"Enter course {i+1}: ")
        courses.append(course)

    student_data = {
        'name': name,
        'age': age,
        'gender': gender,
        'courses': courses
    }
    print("\nStudent bio-data:")    
    print(f"Name: {student_data['name']}")
    print(f"Age:\t{student_data['age']}")
    print(f"Gender:\t{student_data['gender']}")
    print("Courses:")
    for course in student_data['courses']:
        print(f"\t{course}")
collect_student_data()

