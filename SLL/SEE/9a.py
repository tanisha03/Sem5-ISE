class Student:
    def __init__(self):
        self.name=""
        self.age=0
        self.marks=[]
    def display(self):
        print("Name:", self.name)
        print("Age:",self.age)
        print("Marks:", self.marks)
    def insert(self):
        print("enter name")
        name=input()
        self.name=name
        print("enter age")
        age=int(input())
        self.age=age
        print("enter marks in three subjects")
        marks=[]
        for i in range(3):
            marks.append(int(input()))
        self.marks=marks

a=Student()
b=Student()
a.insert()
b.insert()
a.display()
b.display()