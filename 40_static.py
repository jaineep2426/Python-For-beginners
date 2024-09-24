class Employee:
    salary=12000000 #Class Attribute
    language="Python"

    @staticmethod
    def getInfo():
        print("Good Morning")

jainee=Employee()    
jainee.language="Machine Learning"  #Object(Instance) Attribute
print(jainee.language , jainee.salary)
jainee.getInfo()      