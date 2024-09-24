#Create class employee and add salary and increament properties to it.Write a method 'salaryAfterIncrement' method with a @property decorater with a setter which changes the value of increment based on the salary.

class Employee:
    salary = 234
    increament = 20
    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increament/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self , salary):
        self.increament=((salary/self.salary)-1)*100

e=Employee()
#print(e.salaryAfterIncrement)
e.salaryAfterIncrement=280
print(e.increament)

