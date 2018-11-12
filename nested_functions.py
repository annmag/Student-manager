# Nested functions and closures
# Used when you want to delegate a certain task that is only going to be used in one function
# You simply declare a nested (or inner) function in an outer function
# Closure - nested functions does have access to the variables defined in the outer function


def get_students():
    students = ["remus", "james", "sirius"]

    def get_students_title_case():
        students_title_case = []
        for student in students:
            students_title_case.append(student.title())
        return students_title_case

    students_title_case_names = get_students_title_case()
    print(students_title_case_names)


get_students()
