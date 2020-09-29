import random
# print(randNo)
# For comp 1 is rock 2 is Scissor and 3 is paper
# The computer is choosing
randNo = random.randint(1,3)
if randNo == 1:
    comp = 'rock'
elif randNo == 2:
    comp = 'Scissor'
elif randNo == 3:
    comp = 'paper'
# print(comp)


# Function for player
# 1 = rock 2 = Scissor, 3 = paper
def player(play):
    if play == 'r' and comp == 'rock':
        play= 'Rock'
        return 0
    elif play == 's' and comp == 'Scissor':
        play = 'Scissor'
        return 0
    elif play == 'p' and comp == 'paper':
        play = 'Paper'
        return 0
    elif play == 'r' and comp == 'Scissor':
        play == 'Rock'
        return 1
    elif play == 'r' and comp == 'paper':
        play == 'Rock'
        return -1
    elif play == 's' and comp == 'rock':
        play = 'Scissor'
        return -1
    elif play == 's' and comp == 'paper':
        play = 'Scissor'
        return 1
    elif play == 'p' and comp == 'rock':
        play = 'Paper'
        return 1
    elif play == 'p' and comp == 'Scissor':
        play = 'Paper'
        return -1
    else:
        return None

# Taking and  Making the name beautiful
inp = input("Enter 'r' (Rock) or 's' (Scissor) or 'p' (Paper): ")
play = player(inp)

if inp == 'r':
    input_by_the_user = 'Rock'
elif inp == 's':
    input_by_the_user = 'Scissor'
elif inp == 'p':
    input_by_the_user = 'Paper'
input_by_the_computer = comp.capitalize()


# Printing the result...
if play == 0:
    print(f'Computer choose {input_by_the_computer} and you choose {input_by_the_user}. Game draw')
elif play == 1:
    print(f'Computer choose {input_by_the_computer} and you choose {input_by_the_user}. You won')
elif play == -1:
    print(f'Computer choose {input_by_the_computer} and you choose {input_by_the_user}. You loose')
else:
    print("Invlaid Input!!! ")