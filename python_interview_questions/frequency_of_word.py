def freq_words():
    str = input("Enter the string: ")
    li = str.split()
    d = {}

    for i in li:
        if i not in d.keys():
            d[i] = 0
        d[i] = d[i] + 1
    print(d)

freq_words()    

"""
String:

Sheena loves eating apple and mango. Her sister also likes eating 
apple and oranges.
"""