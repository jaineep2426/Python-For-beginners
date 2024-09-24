class employee:
    
        a=1
        @classmethod
        def method(cls):
                print(f"The class attribute is {cls.a}")

e=employee()
e.a=40

e.method()                
