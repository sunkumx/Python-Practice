#Non recursice way!

num = int(input("Enter the number to find the factorial: "))
factorial = 1

if (num < 0):
    print("Given number is negative")

elif (num == 0) or (num == 1):
    print("Factorial of the given number is 1")

else:
    for i in range(1, num+1):
        factorial *= i

    print(f"The factorial of the {num} is {factorial}")



#Finding the factorial of the number using RECURSION
def factorial(x):
    if (x == 1):
        return 1
    else:
        return x * factorial(x-1)

number = int(input("Enter the number to find the factorial: "))
result = factorial(number)

#Using F-String
# print(f"Factorial of {number} is {result}.") 

#Using format for printing the output
print("Factorial of the entered number {} is {}".format(number,result))
