# This file contain HighSchoolStudent class

from student import *  # Importing everything from student.py file


class HighSchoolStudent(Student):

    school_name = "Riverdale High School"

    def get_school_name(self):
        return "Student of Riverdale High School"

    def get_name_capitalize(self):
        original_value = super().get_name_capitalize()
        return original_value + " HS"
