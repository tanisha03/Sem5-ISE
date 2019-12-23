class Sentence:
    vow=['a','e','i','o','u']
    s=""
    rev=""
    def __init__(self,a):
        self.s=a
        self.rev=' '.join(reversed(self.s.split())
    # def rev_t(self):
    #     return self.rev
    # def cnt(self):
    #     count=0
    #     for a in self.s:
    #         if(a.lower() in self.vow):
    #             count+=1
    #     return count 

a=input("enter a string")
b=Sentence(a)
print(b)