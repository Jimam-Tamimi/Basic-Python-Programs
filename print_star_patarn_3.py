#Python program to print star 3
n = int(input("Enter a number to generate star pater: "))
print("*"*n)
i = 0
for j in range(1, n-1):
    print('*', end = '')
    print(" "*(n -2), end = '')
    print('*')
print("*"*n)

# * * * * *
# *       *
# *       *
# * * * * *
# 1 = 0
# 2 = 1
# 3 = 3
# 4 = 5
# 5 = 7
# 6 = 9