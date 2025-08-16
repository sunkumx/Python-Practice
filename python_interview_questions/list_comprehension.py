"""
Link: 
- https://www.w3schools.com/python/python_lists_comprehension.asp
- https://www.geeksforgeeks.org/python/python-list-comprehension/
- 
"""



"""
LIST COMPREHENSION

List comprehension offers a shorter syntax when you want to create a new list based on the values of existing list.

Syntax:


"""

#Example - 1
#Explanation: Returns only those strings which contains letter "a"

#WITHOUT LIST COMPREHENSION

fruits = ["apple","banana","cherry","kiwi","mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

#WITH LIST COMPREHENSION

fruits = ["apple","banana","cherry","kiwi","mango"]
newlist = [x for x in fruits if "a" in x ]
print(newlist)
