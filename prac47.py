#create a class Programmer to storing information of few programmers working at Microsoft.

class Programmer:
    company="Microsoft"

    def __init__(self , name , salary , pincode) :
        self.name=name
        self.salary=salary
        self.pincode=pincode
        
        
p=Programmer("Jainee Patel" , 12000000 , 382421)
print(p.name , p.salary , p.pincode , p.company)
r=Programmer("Rudra Patel" , 15000000 , 382521)
print(r.name , r.salary , r.pincode , r.company)


        

   