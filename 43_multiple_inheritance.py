class Employee:
    company ="Google"
    name="Jainee"
    def show(self):
        print(f"The company salary is {self.name} and language is {self.company}")

class coder:
    language="Python"
    def showlanguage(self):
        print(f"The language is : {self.language}")   

class Manager(Employee , coder):
    company ="Microsoft"
    def showname(self):
      print(f"The company name is {self.company}")
a=Employee()
b=Manager()

b.showlanguage()
b.showname()
b.show()