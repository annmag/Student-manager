# Beginnings of building an app - Student-manager

students = []  # List initialization


def get_students_title_case():
    students_title_case = []
    for student in students:
        students_title_case.append(student["name"].title())  # .title() - the 1st character of every word is capitalized
    return students_title_case


def print_students_title_case():
    students_title_case = get_students_title_case()  # This function calls the function declared above
    print(students_title_case)


def add_student(name, student_id=0):  # Default student_id value is 155 so this argument isn't required
    student = {"name": name, "student_id": student_id}
    students.append(student)
# name and student_id are local variables


def write_to_file(student):
    try:
        file = open("students.txt", "a")  # Opening the student.txt file in appending access mode
        file.write(student + "\n")        # Writing to that file
        file.close()                      # Closing file
    except Exception:
        print("The file can't be saved")


def read_file():
    try:
        file = open("students.txt", "r")  # Opening the student.txt file in reading access mode
        for student in file.readlines():
            add_student(student)
        file.close()
    except Exception:
        print("The file can't be read")


# add_student(name="eva", student_id=345)  # Named arguments, useful with third-party libraries and APIs

read_file()
print_students_title_case()

decision = "Y"

while decision:
    decision = input("Do you want to add new student (Y/N)?: ")
    if decision.upper() == "Y":
        student_name = input("Enter student name: ")
        student_id = int(input("Enter student ID: "))
        add_student(student_name, student_id)
        write_to_file(student_name)
    elif decision.upper() == "N":
        print_students_title_case()
        break
    else:
        print("Undefined answer")
