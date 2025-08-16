#find the common element in the both and return as new list

#Using tuple
a = [1, 2, 3, 1, 2, 1]
b = [1, 4, 5, 1, 1, 2]

set_a = set(a)
set_b = set(b)

common_element = list((set_a & set_b))

print(common_element)

# Using for for loop
b_copy = b.copy()

common_element_list = []

for element in a:
    if element in b_copy:
        common_element_list.append(element)
        b_copy.remove(element)

print(common_element_list)        

