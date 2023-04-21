class cal:
    def __init__(self,num):
        self.num = num
            
    def root(self):
        print(f"Square Root is {self.num **0.5}")
        
    def number(self):
        print(f"Number is {self.num}")
        
    def square(self):
        print(f"Square is {self.num **2}")
        
    def cube(self):
        print(f"Square Root is {self.num **3}")
        

c = cal(9)
c.root()
c.number()
c.square()
c.cube()