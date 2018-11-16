# Comments in Python
# One-line comments creating with pound key (#)

# Multiline comments - a string seprated by three times quotes, not assigned to any variable
# In functions and classes - description in their's bodies

students = []


def add_student(name, student_id=0):
    """
    Adds the student to the students list
    :param name: string - student name
    :param student_id: integer - optional student ID number
    """
    student = {"name": name, "student_id": student_id}
    students.append(student)


add_student("Betty", 222)
print(students)
