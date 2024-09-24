class Employee:
    salary=12000000 #Class Attribute
    language="Python"
    name="Jainee Patel"

    def __init__(self,name , salary , language): #dunder method which is automatically called 
        self.name=name
        self.salary=salary
        self.language=language
        print("This is my object")
        
    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")
    def greet(self):
        print("Good Morning")

jainee=Employee("Jainee Patel" , 18000000 , "Gujarati")    
jainee.language="Machine Learning"  #Object(Instance) Attribute
print(jainee.name , jainee.salary , jainee.language)
#jainee.getInfo()
jainee.greet()
Employee.getInfo(jainee)

#patel=Employee()