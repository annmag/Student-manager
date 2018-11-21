class Kiddo:
    """ This is a class representing children"""

    institution = "Ana's & Mikey's kindergarten"

    def __init__(self, name, age):
        """
        Initialization
        :param name: string - kiddo's name
        :param age: integer - kiddo's age
        """
        self.name = name
        self.age = int(age)

    def __str__(self):
        return "I hide from you kiddos's reference !"

    def get_institution(self):
        return self.institution

    def get_name_capitalize(self):
        return self.name.capitalize()

    def calculate_year_of_birth(self):
        return 2018 - self.age


list_of_kiddos = []
decision = "Y"

while decision:
    decision = input("\nDo you want to add a new kiddo sweetheart? Y/N ")
    if decision.upper() == "Y":
        name = input("Type kiddo's name: ")
        age = input("Type kiddo's age: ")
        list_of_kiddos.append(name)
        new_kiddo = Kiddo(name, age)
        print(new_kiddo.get_name_capitalize() + " - this kiddo has from now a membership in " + Kiddo.institution)
        date = new_kiddo.calculate_year_of_birth()
        print("She or he was born in ")
        print(date)
    elif decision.upper() == "N":
        print("Okay, so enough kiddos in our property!\nThere's a list of all our sweeties:")
        for kiddo in list_of_kiddos:
            print(kiddo)
        break
    else:
        print("I do not know what do you want ! Again!")

