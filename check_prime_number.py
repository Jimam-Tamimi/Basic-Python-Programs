# Python program to check whetear a number is Prime or not
num = int(input("Enter a number to check whether it is not prime or not: "))

check = True
for n in range(2, num):
    if num%n == 0:
        check = False
        break

if num < 2:
    print(f'{num} is not a prime number.')

elif check == True:
    print(f'{num} is a prime number.')
else:
    print(f'{num} is not a prime number.')
