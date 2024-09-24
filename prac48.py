#Write a class "Calculator" capable of finding square , cube or root of number.

class Calculator:
    def __init__(self , n):
        self.n=n

    def square(self):
            print(f"The Square is {self.n * self.n}")
    def cube(self):
                print(f"The Cube is {self.n * self.n * self.n}")
    def root(self):
                    print(f"The Root is {self.n ** (1/2)}")

c= Calculator(4)    
c.square()
c.cube()
c.root()                
        
        