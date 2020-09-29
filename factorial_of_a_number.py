# Program to find factorial of first a number
inp = int(input("Enter a number: "))
i = 1
factorial = 1
while i <= inp:
    factorial = factorial*i
    i+=1
print(f'The factorial of {inp} is {factorial}.')
