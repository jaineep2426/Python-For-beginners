class Employee:
    salary=12000000 #Class Attribute
    language="Python"


jainee=Employee()    
jainee.name="Jainee Patel"  #Object(Instance) Attribute
print(jainee.name ,jainee.language , jainee.salary)

rudra=Employee()
rudra.name="Rudra Patel"
print(rudra.name , rudra.language , rudra.salary)

#Here name is an Object Attribute and salary and languages are class attributes as they directly belong to the class