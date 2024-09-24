#Add the static method in prac48.To greet the user with Hello.

class Calculator:
    def __init__(self , n):
        self.n=n

    def square(self):
            print(f"The Square is {self.n * self.n}")
    def cube(self):
                print(f"The Cube is {self.n * self.n * self.n}")
    def root(self):
                    print(f"The Root is {self.n ** (1/2)}")
    @staticmethod                
    def greet():
            print("Hello World!")                

c= Calculator(4)    
c.square()
c.cube()
c.root() 
c.greet()               
        
        
