def is_prime(number, divisor=2):
    if number <= 2:
        return number == 2
    if number % divisor == 0:
        return False
    if divisor * divisor > number:
        return True
    return is_prime(number, divisor + 1)

num = int(input("Enter the number: "))
if is_prime(num):
    print(f"Entered number {num} is Prime number.")
else:
    print(f"Entered number {num} is not a Prime number.")


    

