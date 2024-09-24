class Employee:
    salary=12000000 #Class Attribute
    language="Python"
    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")
    def greet(self):
        print("Good Morning")

jainee=Employee()    
jainee.language="Machine Learning"  #Object(Instance) Attribute
print(jainee.language , jainee.salary)
#jainee.getInfo()
jainee.greet()
Employee.getInfo(jainee)