#Finding the factorial of the number using RECURSION


def factorial(x):
    if (x == 1):
        return 1
    return x * factorial(x-1)

number = int(input("Enter the number to find the factorial: "))
result = factorial(number)

#Using F-String
# print(f"Factorial of {number} is {result}.") 

#Using format for printing the output
print("Factorial of the entered number {} is {}".format(number,result))
