#Using count method
s = "hello world"
char_to_count = input("Enter the character to count")
count = s.count(char_to_count)
print(count)

#Using LOOP
s = "hello word"
char_to_count = input("Enter the character to count")
count = 0
for char in s:
    if char == char_to_count:
        count =+ 1
print(count)

#Using collection.counter
from collections import Counter

s = "Hello World"
counter = Counter(s)
print(counter)