#For loop syntax, use and tutorials
#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)

"""
NOTE: 

USE: 


Syntax:

for variable in iterable:
    #code block to be executed for each time in the iterable
    # this code must by intented

"""

#Example:

fruits = ["apple", "banana","cherry"]
for fruit in fruits:
    print(fruit)


#Break Statement
#Break Statement - Breaks the statement if true

#Example 1: Loop breaks after the iteration
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#Example 2:Loops breaks when the if condition is true
aplhabets = ["A", "B","C"]
for x in aplhabets:
    if x == "B":
        break
    print(x)

#Continue Statement
#Example 1: Stops the current iteration of loop and continue with next; it skips what ever is in the if statement
fruits = ["Apple", "Banana", "Cherry"]
for x in fruits:
   if x =="Banana":
      continue
   print(x)    
"""
why is it used?
    1. Skipping specific value or condition
    2. Optimizing the loop performance -- by avoiding and processing only particular item
    3. Improving code readability -- 
"""

#Range function


#Else in for loop
#Nest For Loop
#Pass Statement
