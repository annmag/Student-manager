# Dealing with classes

students = []

"""
class Student:

    def add_student(self, name, student_id):
        student = {"name": name, "student_id": student_id}
        students.append(student)


student = Student()
student.add_student("Mark", 123)
print(students)
"""


class Student:

    school_name = "Riverdale Elementary"  # Class attribute - the same across all instances, it's static

    def __init__(self, name, student_id=0):
        """
        This is a constructor method, it's executed every time you create a new instance
        :param name: string - student name
        :param student_id: integer - optional student ID number
        """
        self.name = name  # This two are instance attributes, concern specific instance
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        """
        This method is going to be called every time you print an instance of that class
        :return: string
        """
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()  # Refer to the instance attribute

    def get_school_name(self):
        return self.school_name


class HighSchoolStudent(Student):  # Pattern of inheritance: DerivedInstance(ParentInstance)

    school_name = "Riverdale High School"  # Overriding the class attribute

    def get_school_name(self):
        return "Student of Riverdale High School"  # Overriding the parent method

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()  # super - overriding but still executing the parent method
        return original_value + " HS"


mark = Student("Mark")
print(mark)  # Without str method it's printing a reference to an object at given location in memory
print(Student.school_name + "\n")  # Refer to the class attribute

james = HighSchoolStudent("james")
print(james.get_name_capitalize())
