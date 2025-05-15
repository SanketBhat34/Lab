def factorial(num):
    if num < 0:
        return "Factorial does not exist for negative numbers"
    elif num == 0:
        return 1
    else:
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        return fact
number = int(input("Enter a number: "))
print(f"The factorial of {number} is {factorial(number)}")
