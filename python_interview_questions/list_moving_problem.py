#Moving the Zeros to the end of the list

list = [1,2,0,4,5,0,4,0]

for item in list:

    if item == 0:
        list.remove(item)
        list.append(item)


print(list)