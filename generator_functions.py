# Generator function - a way of crating iterators (objects which you can iterate over)
# Creating generator - defining function with at least one yield statement (or more) instead of return statement
# Difference: return terminates a function entirely
# yield pauses the function saving all it's states and continues there on successive calls
# Once the function yields, the function is paused and the control is transferred to the caller

students = []


def read_students(file):  # This is a generator function
    for line in file:     # For loop - to iterate over the file
        yield line


def read_file():
    try:
        file = open("students.txt", "r")
        for student in read_students(file):  # For loop - to go through all the results from called function
            students.append(student)         # and add them to the list
        file.close()
    except Exception:
        print("The file can't be read")


read_file()
print(students)
