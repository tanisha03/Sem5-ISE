from functools import reduce

list1 = [4, 2, 1, 9, 7, 8]
list2 = [x * 3 for x in list1]
sum = reduce((lambda x, y: x + y), list1)  # reduce(function, sequence)
print("Sum of list 1 is", sum)
print(list2)
sum = reduce((lambda x, y: x + y), list2)
print("Sum of list 1 is", sum)

