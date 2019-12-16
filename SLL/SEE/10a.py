a=[1,23,8,34,17,4]
b=[i*3 for i in a]
print(b)
sum1=reduce((lambda x,y: x+y),a)
print(sum1)
sum2=reduce((lambda x,y: x+y),b)
print(sum2)