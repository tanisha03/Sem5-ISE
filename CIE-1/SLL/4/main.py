import sys 
import os 
from functools import reduce

dict={}

if(len(sys.argv)!=3):
    print("Invalid arguments")
    sys.exit()

if(not(os.path.exists(sys.argv[1]))):
    print("Invalid path")
    sys.exit()

if(sys.argv[2].split('.')[-1]!='txt'):
    print("Invalid file")
    sys.exit()

with open(sys.argv[2]) as file:
    for line in file:
        for word in line.split():
            dict[word]=dict.get(word,0)+1

t=sorted([(v,k) for k,v in dict.items()],reverse=True)
# print(t)
l1=[]

for p in t[0:10]:
    print(p[1])
    l1.append(len(p[1]))

print(l1)

sum=reduce((lambda x,y:x+y),l1)
print("Averaga is ",sum/len(word))

print([x*x for x in l1 if x%2!=0])

