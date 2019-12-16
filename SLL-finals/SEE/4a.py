class Rectangle:
    def __init__(self,a,b):
        self.len=a
        self.breadth=b
    def area(self):
        return self.len*self.breadth

rec=Rectangle(4,5)
print(rec.area())