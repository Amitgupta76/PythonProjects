import random
print("Welcome to the Number Guessing Game!\n")
print("I'm thinking of a number between 1 and 100.")
choose = input("Choose a difficulty. Type 'easy' or 'hard': ")
number = random.randint(1,101)
if choose == "easy":
    a=10
    game = False
    while(a>0 and not game):
        print(f"You have {a} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if(guess > number):
            print("Too high.")
            print("Guess again.")
        elif(guess<number):
            print("Too low.")
            print("Guess again.")
        elif(guess == number):
            print(f"You got it! The answer was {number}.")
            game = True
        a-=1
    if(a==0 and not game):
        print("You lose!")

if choose == "hard":
    a=5
    game = False
    while(a>0 and not game):
        print(f"You have {a} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if(guess > number):
            print("Too high.")
            print("Guess again.")
        elif(guess<number):
            print("Too low.")
            print("Guess again.")
        elif(guess == number):
            print(f"You got it! The answer was {number}.")
            game = True
        a-=1
    if(a==0 and not game):
        print("You lose!")