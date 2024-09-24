#Create a class "PET" from class "ANIMALS" and further create a class "DOG" from "PETS" . Add a method "BARK" to class "DOG"


class Animals():
    pass

class Pets(Animals):
    pass

class Dogs(Pets):
    @staticmethod
    def Bark():
        print("Bow Bow")


d=Dogs()
d.Bark()