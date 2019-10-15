class Sentence_rev:
    s=""
    rev_s=""
    vowels=['a','e','i','o','u']
    def __init__(self,sentence):
        self.s=sentence
        self.rev_s=' '.join(reversed(self.s.split()))
    def ret_rev(self):
        return self.rev_s
    def count_vow(self):
        return sum(s in self.vowels for s in self.s.lower())

l1=[]

for i in range(3):
    reverser=Sentence_rev(input("enter a string\n"))
    l1.append(reverser)
    # print(reverser.ret_rev())
    # print(reverser.count_vow())
    # print()

for i in sorted(l1,key=lambda i:i.count_vow(),reverse=True):
    print(i.ret_rev())

