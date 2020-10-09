
from random import randint
num = randint(1, 100)
print(num)
i = 0
userNum = int(input("Enter a number: "))
while True:
    i+=1
    if userNum < num:
        result = False
        userNum = int(input('Higher number please: '))
    elif userNum > num:
        result = False
        userNum = int(input('Lower number please: '))
    elif userNum == num:
        break
        print(f"\nYou have won and the number is {num}.\nTotal {i} moves taken.")

with open("highscore.txt", "r") as f2:
    data = int(f2.read())
if i < data:
    with open("highscore.txt" , "w") as f:
        f.write(str(i))
   
# with open("highscore.txt", "r") as f:
#     hiscore = int(f.read())

# if(i<hiscore):
#     print("You have just broken the high score!")
#     with open("highscore.txt", "w") as f:
#         f.write(str(i))