"""

find the common letter in the string bellow

NAINA
REENE

"""

def common_letters():
    str1 = input("Enter the first string")
    str2 = input("Enter the second string")
    s1 = set(str1)
    s2 = set(str2)
    print(s1)
    print(s2)
    com_letter = s1 & s2
    print("Common letters are :", com_letter)


common_letters()