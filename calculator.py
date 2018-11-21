# Simple calculator

history = []
decision = 1


def adding(number_1, number_2):
    return number_1 + number_2


def subtracting(number_1, number_2):
    return number_1 - number_2


def multiplying(number_1, number_2):
    return number_1 * number_2


def dividing(number_1, number_2):
    try:
        dividing_result = number_1 / number_2
        return dividing_result
    except ZeroDivisionError:
        print("You cannot divide by zero")


def equation_string(argument_1, argument_2, argument_3, argument_4):
    """
    Printing and returning a string which is presenting an equation
    :param argument_1: integer - first number in mathematical operation
    :param argument_2: string - sign of mathematical operation
    :param argument_3: integer - second number in mathematical operation
    :param argument_4: integer - result of an mathematical operation
    :return: string - an equation
    """
    equation = str(argument_1) + argument_2 + str(argument_3) + "=" + str(argument_4)
    print(equation)
    return equation


def writing_to_file(list_of_elements):
    try:
        file = open("calculator.txt", "a")
        for list_element in list_of_elements:
            file.write(list_element + "\n")
        file.close()
    except Exception:
        print("Some problem with file has occurred")


while decision:

    print("\nChoose operation:\n"
          "1 - add\n"
          "2 - subtract\n"
          "3 - multiply\n"
          "4 - divide\n"
          "5 - show latest history\n"
          "6 - end calculations\n"
          )
    decision = input("Your choice: ")

    if decision == "1" or decision == "2" or decision == "3" or decision == "4":

        first_number = int(input("Type the first number: "))
        second_number = int(input("Type the second number: "))

        if decision == "1":
            result = adding(first_number, second_number)
            history.append(equation_string(first_number, "+", second_number, result))
        elif decision == "2":
            result = subtracting(first_number, second_number)
            history.append(equation_string(first_number, "-", second_number, result))
        elif decision == "3":
            result = multiplying(first_number, second_number)
            history.append(equation_string(first_number, "*", second_number, result))
        elif decision == "4":
            result = dividing(first_number, second_number)
            if result:
                history.append(equation_string(first_number, "/", second_number, result))

    elif decision == "5":
        for element in history:
            print(element)
    elif decision == "6":
        writing_to_file(history)
        break
    else:
        print("Unknown operation type")
