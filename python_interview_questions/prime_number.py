#Prime number is number which is divisible by 1 or itself

num = int(input("Enter the number to check whether it is prime or not: "))
prime = 1
for x in range(2, num):
    if(num % 2 == 0):
        prime = 2
if(prime == 1):
    print("Entered number is prime number")
else:
    print("Not a prime number!")