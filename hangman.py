import random
word_list = ["ardvark", "baboon", "camel"]
word = random.choice(word_list)
list = []
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

for i in range(0, len(word)):
    list.append("_")
    
end = 5
end_game = False
while end>=0 or not end_game:
    guess=input("Guess a letter: ").lower()
    if guess in word:
        for i in range(0,len(word)):
            if(word[i]==guess):
                list[i] = guess
    else:
        print(stages[end])
        end-=1
        if(end == -1):
            end_game = True
            print("You lose")
    print(list)
    if "_" not in list:
        end_game = True
        end = -1
        print("You Win")
    

        

