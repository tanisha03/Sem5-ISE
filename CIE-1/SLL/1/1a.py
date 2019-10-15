l1=[]

def read_ele():
    for i in range(6):
        l1.append(int(input("enter a number\n")))

def rem_dup():
    return list(set(l1))


def even_list():
    l3=[i for i in l1 if i%2==0]
    return l3 

def rev_list():
    return l1[::-1]

read_ele()
print(l1)
print(rem_dup())
print(even_list())
print(rev_list())