print("enter intergers separated by space")
a=input().split() #separate elements by space
arr=[int(i) for i in a] #convert each to integer
print("Max :", max(arr))
print("Min :", min(arr))
print("enter element to be inserted")
i=int(input())
arr.append(i)
print("enter element to be deleted")
i=int(input())
arr.remove(i)
print("enter element to be searched")
i=int(input())
if(i in a):
    print("present")
else:
    print("Not present")
