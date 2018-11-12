def var_args(name, *args):  # Function with variable number of arguments
    print(name)
    print(args)  # args is a list!


def k_var_args(name, **kwargs):  # The keys of the dictionary are the names of arguments you pass
    print(name)
    print(kwargs["birth_date"], kwargs["field_of_study"])  # kwarg is a dictionary!


print("Hello students", 1000, True, "Hard studies", None)  # print function can have many arguments
var_args("Julie", 1996, False, "Biology")
k_var_args("Jenna", birth_date=1997, feedback=None, field_of_study="Mathematics")