#Write a python program to read in a list of elements.
#Create a new list that holds all the elements minus the duplicates (Use functions).
def remove_duplicates(numbers):
    newlist = []
    for number in numbers:
       if number not in newlist:
           newlist.append(number)
    return newlist
remove_duplicates([1,2,3,4,5,5,5,6,3,2])

#Write a python program to read in a list of numbers.
#Use one-line comprehensions of create a new list of even numbers.
#Create another list reversing the elements.
S = [x**2 for x in range(10)] # read elements  to list
M = [x for x in S if x % 2 == 0]
M.reverse()

#Write a python program to count the frequency of words in a given file.
from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count("test.txt"))


#!/usr/bin/env python
#Introduction to Python : Classes & Objects, Functions
#b)   Write a recursive python function that has a parameter representing a list of integers
#and returns the maximum stored in the list.
#Hint: The maximum is either the first value in the list or the maximum of the rest of
#the list whichever is larger. If the list only has 1 integer, then its maximum is this
#single value, naturally. Demonstrate with some examples.

# Note : Handle all other corner cases which are not handled here

def Max(list):
    if len(list) == 1:
        return list[0]
    else:
        m = Max(list[1:])
        return m if m > list[0] else list[0]

def main():
	try:
		list = eval(input("Enter a list of numbers: "))
		print ("The largest number is: ", Max(list))
	except SyntaxError:
		print ("Please enter comma separated numbers")
	except:
		print ("Enter only numbers")

main()
