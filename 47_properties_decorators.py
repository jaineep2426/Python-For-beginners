class employee:
    
        a=1
        @classmethod
        def method(cls):
                print(f"The class attribute is {cls.a}")

        @property
        def name(self):
                return f"{self.fname} {self.lname}"

        @name.setter
        def name(self , value):
                self.fname=value.split(" ")[0]  
                self.lname=value.split(" ")[1]       

e=employee()
e.a=40

e.name="Jainee Patel"
print(e.fname , e.lname)
e.method()       