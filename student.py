# This file contains Student class

students = []


class Student:
    """
    This is parent class
    """

    school_name = "Riverdale Elementary"

    def __init__(self, name, last_name, student_id=0):
        """
        This is a constructor method, it's executed every time you create a new instance
        :param name: string - student name
        :param last_name: string - student last name
        :param student_id: integer - optional student ID number
        """
        self.name = name
        self.last_name = last_name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        """
        This method is going to be called every time you print an instance of that class
        :return: string
        """
        return "Student " + self.name

    def get_name_capitalize(self):
        """
        This method returns capitalized student name
        :return: string - capitalized student name
        """
        return self.name.capitalize()

    def get_school_name(self):
        """
        This method returns school name
        :return: string - school name
        """
        return self.school_name
