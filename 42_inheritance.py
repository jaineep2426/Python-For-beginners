class Employee:
    company ="Google"
    def show(self):
        print(f"The company salary is {self.salary} and language is {self.language}")

#class Manager:
   # company ="Microsoft"
   #def show(self):
    #    print(f"The company salary is {self.salary} and language is {self.language}")   

   # def showname(self):
   #     print(f"The company name is {self.name}")      

class Manager(Employee):
    company ="Microsoft"
    def showname(self):
      print(f"The company name is {self.name}")
a=Employee()
b=Manager()

print(a.company , b.company)
