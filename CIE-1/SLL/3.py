class Sentence_rev:
    s=""
    rev_s=""
    vowels=['a','e','i','o','u']
    dic={}
    desc_str=[]
    def __init__(self,sentence):
        self.s=sentence
        self.rev_s=' '.join(reversed(self.s.split()))
    def ret_rev(self):
        return self.rev_s
    def count_vow(self):
        self.dic={}
        self.desc_str=[]
        for i in self.s.split():
            count=sum(s in self.vowels for s in i)
            self.dic[i]=count
        # print(self.dic)
        for i in sorted(self.dic.values(),reverse=True):
            for x in self.dic.keys():
                if self.dic[x]==i:
                    self.desc_str.append(x)
                    break
        return ' '.join(self.desc_str)
        # return self.desc_str

for i in range(3):
    reverser=Sentence_rev(input("enter a string\n"))
    print(reverser.ret_rev())
    print(reverser.count_vow())
    print()