def ret_max(l1):
    if(len(l1)==1):
        return l1[0]
    else:
        return max(l1[0],ret_max(l1[1:]))

l1=[]
for i in range(5):
    l1.append(int(input("enter a number\n")))

print(ret_max(l1))
