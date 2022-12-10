import random
rock = '''
    _______
___'    ___)
       (____)
       (____)
       (___)        
---,___(__)

'''

paper = '''
    _______
___'    ___ )
       (__________)
       (_____________)
       (___________)        
---,___(_________)

'''

scissors = '''
    _______
___'    ___)
       (__________)
       (_____________)
       (___)        
---,___(__)

'''

game = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game[choice])
print("Computer Chose:")
c=random.randint(0,2)
print(game[c])
if(choice==c):
    print("Draw")
else:
    if choice==0 and c==1 :
        print("Computer Won")
    elif(choice==0 and c==2):
        print("You Won")
    elif(choice==1 and c==2):
        print("Computer Won")
    elif(choice==1 and c==0):
        print("You Won")
    elif(choice==2 and c==0):
        print("Computer Won")
    elif(choice==2 and c==1):
        print("You Won")
    
        
 








